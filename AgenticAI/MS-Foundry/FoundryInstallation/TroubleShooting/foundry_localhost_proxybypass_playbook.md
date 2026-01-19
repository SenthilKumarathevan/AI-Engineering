# Runbook: Fixing Foundry Local CLI Failures Caused by Corporate Proxy (Windows 11)

Engineers using **Foundry Local Model Server + `foundry` CLI** on **Windows 11**, particularly on corporate networks or VPNs with enforced proxy settings.

---

## Symptoms

One or more of the following:

### A) Catalog / list failure (JSON parse error)

Running:

```powershell
foundry model list
````

Returns an error similar to:

```
Exception failure fetching models from Azure Foundry catalog. '<' is an invalid start of a value ...
```

**Interpretation:**
The CLI expected **JSON** from the Azure catalog but received **HTML** (commonly a proxy block page, login portal, or intercept page beginning with `<html...>`).

---

### B) Local service connectivity failure (localhost call is proxied)

Running:

```powershell
foundry service status
foundry model list
```

Returns an error similar to:

```
Exception: Request to local service failed. URI: http://127.0.0.1:<port>/openai/status
No such host is known. User proxy.wip.nbsnet.co.uk:8000.
```

**Interpretation:**
The CLI call to `127.0.0.1` is being routed through the **corporate proxy**, which breaks loopback calls.

---

## Environment / Preconditions

* Windows 11
* Foundry Local installed via **winget**

  * App: `Foundry Local Model Server`
  * ID: `Microsoft.foundry.local`
  * Example version encountered: `0.8.117.0`
* **No assumption of admin rights**

---

## Quick Diagnosis Workflow

### 1) Identify whether the issue is **catalog** or **local service**

Run:

```powershell
foundry model list
```

* If you see `'<‘ is an invalid start of a value` → **catalog call is returning HTML**
* If you see `Request to local service failed ... 127.0.0.1 ... Use proxy ...`
  → **localhost traffic is being proxied (fix this first)**

---

### 2) Confirm whether proxy environment variables exist

Run:

```powershell
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
```

If you see something like:

```
HTTP_PROXY=http://userproxy.wip.nbsnet.co.uk:8000
```

…this is the likely root cause of local service failures.

---

## Resolution (Immediate / Session Fix)

### A) Fix localhost failures in the current PowerShell session

If `HTTP_PROXY` is set and Foundry cannot reach `127.0.0.1`, apply a **session-only bypass**:

```powershell
# Bypass proxies for localhost / loopback (session only)
$env:NO_PROXY  = "localhost,127.0.0.1"
$env:no_proxy  = $env:NO_PROXY

# Remove proxy variables from this session so localhost is not proxied
$env:HTTP_PROXY  = ""
$env:http_proxy  = ""
$env:HTTPS_PROXY = ""
$env:https_proxy = ""

# Re-test
foundry service status
```

**Expected success output:**

```
🟢 Model management service is running on http://127.0.0.1:<port>/openai/status
```

Once this is working, proceed to the persistent configuration.

---

## Persistent Fix (User Scope, No Admin Required)

### Objective

Keep corporate proxy settings available for **internet traffic** but **always bypass proxy for localhost**, so Foundry can consistently reach its local service while VPN is connected.

---

### Apply the persistent fix

Run:

```powershell
# Persist proxy settings for your user (if required for corporate network)
[Environment]::SetEnvironmentVariable("HTTP_PROXY",  "http://userproxy.wip.nbsnet.co.uk:8000", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://userproxy.wip.nbsnet.co.uk:8000", "User")

# Ensure localhost / loopback NEVER uses the proxy
[Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1", "User")
[Environment]::SetEnvironmentVariable("no_proxy", "localhost,127.0.0.1", "User")
```

---

### Validate persistence

1. Close **all** PowerShell windows.
2. Open a **new** PowerShell window.
3. Run:

```powershell
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
foundry service status
foundry model list
```

**Expected:**

* `HTTP_PROXY` / `HTTPS_PROXY` present (if required by your environment)
* `NO_PROXY` / `no_proxy` includes `localhost,127.0.0.1`
* `foundry service status` succeeds
* `foundry model list` succeeds (catalog access may still depend on network policy)

---

## Optional: WinINET Proxy Override (Registry) — Not Sufficient Alone

A WinINET bypass may be configured but does **not always affect tools that rely on environment variables** (as Foundry did here).

If needed for broader Windows apps, you can add loopback to WinINET proxy overrides:

```powershell
$k='HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
$v=(Get-ItemProperty $k -Name ProxyOverride -ErrorAction SilentlyContinue).ProxyOverride
foreach($n in '<local>','localhost','127.0.0.1'){
  if($v -notmatch [regex]::Escape($n)){
    $v=($v.TrimEnd(';')+';'+$n).Trim(';')
  }
}
Set-ItemProperty $k -Name ProxyOverride -Value $v
"ProxyOverride set to: $v"
```

**Note:**
In the incident resolved by this playbook, **WinINET override alone was not sufficient**, because `HTTP_PROXY` environment variables were still forcing proxy usage for `127.0.0.1`. The durable fix was setting `NO_PROXY` and ensuring Foundry’s session did not proxy localhost.

---

## Root Cause Summary

* Corporate proxy environment variables (e.g. `HTTP_PROXY`) were configured.
* Foundry CLI attempted to call its local service endpoint at:

  ```
  http://127.0.0.1:<port>/openai/status
  ```
* The proxy setting caused `127.0.0.1` traffic to be proxied, resulting in:

  * `No such host is known` errors
* Adding `NO_PROXY=localhost,127.0.0.1` (and `no_proxy`) ensured loopback traffic bypassed the proxy, restoring local service communication.
* Persisting those variables at **User scope** made the fix reliable across new PowerShell sessions and while connected to VPN.

---

## Runbook Checklist (Copy / Paste)

### Detect

```powershell
foundry service status
foundry model list
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
```

---

### Fix (Session)

```powershell
$env:NO_PROXY="localhost,127.0.0.1"; $env:no_proxy=$env:NO_PROXY
$env:HTTP_PROXY=""; $env:http_proxy=""
$env:HTTPS_PROXY=""; $env:https_proxy=""
foundry service status
```

---

### Fix (Persistent, User Scope)

```powershell
[Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1", "User")
[Environment]::SetEnvironmentVariable("no_proxy", "localhost,127.0.0.1", "User")

# Optionally preserve corporate proxy if required
[Environment]::SetEnvironmentVariable("HTTP_PROXY",  "http://userproxy.wip.nbsnet.co.uk:8000", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://userproxy.wip.nbsnet.co.uk:8000", "User")
```

---

### Validate (New Terminal)

```powershell
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
foundry service status
foundry model list
```  

**Expected success output:**

```
🟢 Model management service is running on http://127.0.0.1:<port>/openai/status
```
