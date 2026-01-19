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
