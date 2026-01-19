# Persistent Localhost Proxy Bypass (User-Level, No Admin)

## Main goal

Apply a **clean, persistent user-level proxy bypass for localhost** so that:

- Foundry CLI
- Foundry Local service
- Python SDKs (`foundry-local`, OpenAI-compatible clients, `requests`, `httpx`, etc.)

can reliably communicate with `127.0.0.1` **without interference from the corporate proxy**, across **all future sessions**, **without admin rights**, and **without impacting other applications**.

---

## One-liner (PowerShell) — apply Option A cleanly

Run this **once** in PowerShell (no elevation required):

```powershell
$k='HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings';$v=(gp $k ProxyOverride -ea 0).ProxyOverride;foreach($n in '<local>','localhost','127.0.0.1'){if($v -notmatch [regex]::Escape($n)){$v=($v.TrimEnd(';')+';'+$n).Trim(';')}};sp $k ProxyOverride $v;"ProxyOverride set to: $v"
````

---

## What this does (precisely)

* Updates **only** the current user’s WinINET proxy bypass list

* Ensures these entries exist:

  ```
  <local>;localhost;127.0.0.1
  ```

* Does **not**:

  * Disable the corporate proxy
  * Change WinHTTP (machine-level) settings
  * Require admin rights
  * Affect non-localhost traffic

The change is **persistent across reboots and new terminals**.

---

## Quick verification (optional)

Open a **new** PowerShell window and run:

```powershell
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' |
  Select-Object ProxyOverride
```

You should see `localhost` and `127.0.0.1` included.

---


# Eliminating Remaining Proxy Interference for Foundry Local

## Main goal

Eliminate the remaining proxy source (**environment variables or application-level proxy configuration**) that is forcing Foundry to proxy `127.0.0.1`, then confirm that the **local Foundry service** is reachable.

---

## Current diagnosis

Your **ProxyOverride** change is correct for **WinINET**. However, Foundry is still explicitly reporting:

```

Use proxy.wip.nbsnet.co.uk:8000

````

This strongly indicates that:

- The Foundry CLI is **not** relying on WinINET for proxy resolution, and
- It is instead reading:
  - **Proxy environment variables** (`HTTP_PROXY`, `HTTPS_PROXY`, etc.), or
  - A **Foundry-specific application configuration**

Therefore, the next step is to **prove whether proxy environment variables are present** and temporarily neutralise them for the current session.

---

## One-step action (PowerShell)

Open a **fresh PowerShell window**, then run the following exactly.

### 1) Inspect proxy-related environment variables

```powershell
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
````

---

```text
--- Clearing proxy env vars for this session ---
```

---

### 2) Bypass proxies for localhost/loopback for this session

```powershell
$env:NO_PROXY  = "localhost,127.0.0.1"
$env:no_proxy  = $env:NO_PROXY
$env:HTTP_PROXY  = ""
$env:http_proxy  = ""
$env:HTTPS_PROXY = ""
$env:https_proxy = ""
```

---

### 3) Re-test local service connectivity

```powershell
foundry service status
```

---

## What to paste back

After running the steps above, paste:

* The **output of the environment-variable listing** (step 1)
* The **full output** of:

  ```powershell
  foundry service status
  ```

---

## What this proves

If `foundry service status` works after this step, it confirms:

* The proxy was being injected via **environment variables**
* WinINET settings were not the remaining blocker
* Foundry respects session-level proxy environment variables

---

## Next step (if this works)

If service status is successful:

* We will make the bypass **persistent without admin rights** by:

  * Setting **user-level environment variables**, so every new terminal inherits the bypass, and/or
  * Removing the proxy variables at their source (for example, corporate login scripts or shell initialisation)

This ensures the fix is permanent and does not rely on per-session overrides.
