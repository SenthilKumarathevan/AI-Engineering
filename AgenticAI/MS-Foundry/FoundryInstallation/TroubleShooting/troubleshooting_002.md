# Proving the Foundry CLI Catalog Is Returning HTML (Not JSON)

## Main goal

Prove that the **Foundry CLI’s catalog endpoint** is returning **HTML instead of JSON**, and identify the **exact endpoint being called**, so we can remediate the issue **without requiring admin rights**.

---

## Current situation recap

Your proxy configuration is clean:

- No WinHTTP proxy configured
- No per-user IE / WinINET proxy configured

This significantly narrows the likely causes to one of the following:

- **(a)** The Foundry CLI is calling a catalog endpoint that returns an **HTML error page**
- **(b)** An **authentication or captive-portal-style intercept** exists in the environment
- **(c)** The CLI is resolving or constructing an **incorrect base URL** for the catalog

In all cases, the next step is the same: **capture the actual HTTP response the CLI receives** when it attempts to list models.

---

## One-step action (PowerShell)

Run the Foundry CLI with **maximum verbosity** and capture *both stdout and stderr* to a log file.

Run **exactly** the following in PowerShell:

```powershell
$log = Join-Path $env:TEMP ("foundry-model-list-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".log")
& foundry model list --verbose --log-level Debug *>&1 | Tee-Object -FilePath $log
"`nLog saved to: $log"
````

---

## What to paste back

From the generated log file, paste **the last ~120 lines**.

---

## What will be examined in the log

Specifically, the following signals:

* The **catalog URL** being called
  (any line containing `https://...`, especially with `catalog` or `model` in the path)
* **HTTP status codes**:

  * `200`, `301`, `302`, `401`, `403`, `407`, `5xx`
* Any **Content-Type hints**, such as:

  * `text/html`
  * redirects
  * “sign in”, “access denied”, or block-page markers

This will conclusively determine whether the CLI is receiving HTML and from which endpoint.

---

## What happens next (single-step continuation)

Once those log lines are reviewed, the *next single step* will be **one** of the following:

* **Direct `Invoke-WebRequest`** to the *exact catalog URL*
  → to show the first bytes of the response and confirm HTML vs JSON

**or**

* **Adjusting CLI behavior**:

  * switching to an alternate catalog setting
  * disabling catalog fetch
  * using an offline/local-only model list
    (depending on what the log reveals)

---

This step is purely observational and requires **no admin rights**.
