# Foundry Local – Catalog vs Local Inference Failure Validation

## Main goal
Confirm whether the failure is in the **Azure Foundry catalog HTTP call** (returning HTML) versus the **local inference service**, then apply the smallest corrective change.

---

## Key clarification

You are correct that:

- `foundry service diag` reports on the **local inference service** (127.0.0.1, local cache path).
- That output **does not imply** the Foundry CLI will never call an external URL.

The specific error you reported:

```

failure fetching models from Azure Foundry catalog. '<' is an invalid start of a value

````

strongly indicates:

- The CLI **did make an HTTP request** to the Azure Foundry catalog.
- The response was **HTML**, not JSON.
- HTML responses typically start with `<html...>`, which explains the parsing error.

This most commonly occurs due to:
- Proxy block pages
- Captive portals
- Authentication intercept pages
- TLS inspection / corporate security gateways

This means the **failure is almost certainly outside the local inference service**.

---

## One verification step (PowerShell)

Run the following **exactly as-is** in PowerShell and paste the full output.  
This does **not** require admin privileges.

```powershell
$ProgressPreference = 'SilentlyContinue'

# 1) Show proxy configuration that could rewrite HTTPS responses
netsh winhttp show proxy
"`n---`n"
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' |
  Select-Object ProxyEnable, ProxyServer, ProxyOverride, AutoConfigURL

"`n---`n"

# 2) Attempt a simple HTTPS fetch and show status + content-type + first 200 chars
$resp = Invoke-WebRequest -Uri "https://example.com" -MaximumRedirection 0 -ErrorAction SilentlyContinue
if ($resp) {
  "example.com status: $($resp.StatusCode)"
  "example.com content-type: $($resp.Headers.'Content-Type')"
  "example.com first200: " + ($resp.Content.Substring(0,[Math]::Min(200,$resp.Content.Length)) -replace "`r|`n"," ")
} else {
  "example.com request failed: $($Error[0].Exception.Message)"
}

"`n---`n"

# 3) Find the Foundry CLI binary actually being executed
Get-Command foundry | Format-List *
````

---

## What the output will confirm

From the results above, we can conclusively determine whether the issue is:

* **Proxy interception**

  * WinHTTP proxy configured
  * User proxy / PAC file configured
  * HTML returned instead of JSON

* **TLS inspection or certificate interception**

  * HTTPS succeeds
  * Response content-type is `text/html`
  * Content resembles an auth or block page

* **Executable mismatch**

  * Foundry CLI resolves to a WindowsApps shim or unexpected binary
  * Different binary than expected is being executed

---

## What to look for in the output

Specifically:

* Any of the following:

  * `ProxyEnable = 1`
  * `ProxyServer`
  * `AutoConfigURL`
* HTML returned by `Invoke-WebRequest`:

  * `<html>`
  * Login pages
  * Block / access denied pages
* The exact filesystem path returned by:

  ```powershell
  Get-Command foundry
  ```

This is important on Windows due to WindowsApps shims.

---

## Next step (after this verification)

Once the output is reviewed, the corrective action will typically be **one minimal change**, such as:

* Aligning WinHTTP proxy with the user proxy
* Explicitly bypassing proxy usage for the Foundry CLI
* Trusting the corporate TLS inspection root certificate
* Correcting the executable path used by the CLI

No reinstall, no guesswork, and no changes beyond what is strictly necessary.

Paste the output from the PowerShell command block above for the next step.

