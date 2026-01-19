# Restoring Foundry CLI ↔ Local Service Connectivity

## Main goal

Restore **CLI-to-local-service connectivity** by removing the forced corporate proxy for **localhost traffic** and confirming that the **Foundry local service** is running.

---

## Current diagnosis

You have confirmed that the root cause has shifted:

- While **on VPN**, catalog fetch was intercepted.
- While **off VPN**, your machine is still configured with a **user-level proxy**:
```

proxy.wip.nbsnet.co.uk:8000

```
- That proxy is attempting to route requests to:
```

[http://127.0.0.1](http://127.0.0.1):<port>/...

```
- This causes failures such as:
```

No such host is known

````

In short: **localhost traffic is being incorrectly sent through the corporate proxy**, breaking communication with the local Foundry service.

---

## One-step action (PowerShell)

Bypass the proxy for loopback/localhost traffic and restart the Foundry local service.

Run **exactly** the following in PowerShell:

```powershell
# 1) Add localhost/loopback to the current user's proxy bypass list (WinINET)
$regPath = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
$cur = (Get-ItemProperty -Path $regPath -Name ProxyOverride -ErrorAction SilentlyContinue).ProxyOverride
if (-not $cur) { $cur = "" }

# ensure these entries exist
$needed = @('<local>','localhost','127.0.0.1')
foreach ($n in $needed) {
if ($cur -notmatch [regex]::Escape($n)) {
  if ($cur -and $cur[-1] -ne ';') { $cur += ';' }
  $cur += $n
}
}

Set-ItemProperty -Path $regPath -Name ProxyOverride -Value $cur
"ProxyOverride is now: $cur"

# 2) Restart Foundry local service via CLI (no admin required if supported)
foundry service restart
foundry service status
````

---

## What to send back after this step

After running the commands above, paste:

* The full output of:

  ```powershell
  foundry service status
  ```
* Then run and paste the exact output of:

  ```powershell
  foundry model list
  ```

---

## If the restart fails

If `foundry service restart` fails due to permissions or an unsupported command:

* Paste the **exact error message**
* The next step will be the **smallest possible alternative**, such as:

  * process-level restart without admin rights, or
  * a per-process proxy bypass scoped only to the Foundry CLI

This keeps changes minimal and reversible.
