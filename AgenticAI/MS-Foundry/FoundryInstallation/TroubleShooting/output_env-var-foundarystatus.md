```  
PS C:\Users\P432852> foundry service status
Exception: Request to local service failed. Uri:http://127.0.0.1:55064/openai/status
No such host is known. (userproxy.wip.nbsnet.co.uk:8000)
Please check service status with 'foundry service status'.
PS C:\Users\P432852> Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name

Name                           Value
----                           -----
HTTP_PROXY                     http://userproxy.wip.nbsnet.co.uk:8000


PS C:\Users\P432852> $env:NO_PROXY  = "localhost,127.0.0.1"
PS C:\Users\P432852> $env:no_proxy  = $env:NO_PROXY
PS C:\Users\P432852> $env:HTTP_PROXY  = ""
PS C:\Users\P432852> $env:http_proxy  = ""
PS C:\Users\P432852> $env:HTTPS_PROXY = ""
PS C:\Users\P432852> $env:https_proxy = ""
PS C:\Users\P432852> foundry service status
🟢 Model management service is running on http://127.0.0.1:55064/openai/status
EP autoregistration status: Successfully downloaded and registered the following EPs: OpenVINOExecutionProvider, NvTensorRTRTXExecutionProvider, CUDAExecutionProvider.
Valid EPs: CPUExecutionProvider, WebGpuExecutionProvider, OpenVINOExecutionProvider, NvTensorRTRTXExecutionProvider, CUDAExecutionProvider
PS C:\Users\P432852>  
```


# Persisting a Safe Proxy Configuration for Foundry (User-Level, No Admin)

## Main goal

Make **Foundry work reliably** by permanently bypassing the corporate proxy for **localhost traffic**, **without requiring admin rights**, while still keeping the corporate proxy available for external internet access.

---

## Root cause (now confirmed)

You have conclusively proven that:

- The environment variable  
```

HTTP_PROXY=[http://userproxy.wip.nbsnet.co.uk:8000](http://userproxy.wip.nbsnet.co.uk:8000)

```
was being applied to requests targeting:
```

127.0.0.1

````
- This caused Foundry to proxy calls intended for the **local Foundry service**, breaking:
- `foundry service status`
- `foundry model list`
- Clearing the proxy **in-session** immediately restored functionality.

This confirms the issue is **environment-variable–driven**, not WinINET or service-related.

---  

## One-step action (PowerShell)

Persist a **safe, user-scoped proxy configuration** so that:

- Corporate proxy is still used for internet calls
- Localhost (`127.0.0.1`, `localhost`) is **never** proxied

Run the following **once** in PowerShell (no admin rights required):

```powershell
# Persist corporate proxy for internet access (user scope)
[Environment]::SetEnvironmentVariable("HTTP_PROXY",  "http://userproxy.wip.nbsnet.co.uk:8000", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://userproxy.wip.nbsnet.co.uk:8000", "User")

# Ensure localhost / loopback never uses the proxy
[Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1", "User")
[Environment]::SetEnvironmentVariable("no_proxy", "localhost,127.0.0.1", "User")
```

"User env vars set. Close all PowerShell windows and open a new one, then run:"
"  foundry service status"
"  foundry model list"

---

## Required verification

After **closing all PowerShell windows** and opening a **new** one, run and paste the output of:

```powershell
foundry service status
foundry model list
```

---

## Expected outcome

* `foundry service status` succeeds consistently across sessions
* `foundry model list` works when not blocked by catalog-side issues
* Foundry CLI, Foundry Local, and Python SDKs can all communicate with
  `127.0.0.1` reliably

---

## If issues remain on VPN

If `foundry model list` still fails **on VPN** with the original JSON/HTML parsing error:

* That indicates a **catalog-side interception** (proxy / TLS inspection returning HTML)
* This will be addressed **only after** confirming localhost stability across sessions

At this point, localhost connectivity is correctly and permanently fixed at the user level.  

---  

# Locking in a Stable Foundry Local Configuration (VPN)

## Main goal

Lock in a **stable Foundry Local configuration while on VPN** by:

1. Ensuring **localhost traffic always bypasses the corporate proxy**
2. Validating **both local-service and catalog operations end-to-end**

---

## Next (single) step

Validate both paths and capture a **minimal runbook trace**.

Open a **new PowerShell window** with **VPN connected**, then run the following commands **exactly** and paste the full output.

---

### 1) Confirm proxy environment variables for this session

```powershell
Get-ChildItem Env: | Where-Object Name -match 'PROXY|NO_PROXY' | Sort-Object Name
````


### 2) Confirm local Foundry service connectivity

```powershell
foundry service status
```

---

### 3) Confirm model catalog access

```powershell
foundry model list
```

---

## How to interpret the results

* **If `foundry model list` still returns**

  ```
  '<' is an invalid start of a value
  ```

  then:

  * Local service connectivity is fixed
  * The remaining issue is **catalog-side** (proxy or TLS inspection returning HTML)
  * Next steps will focus exclusively on the catalog HTTP path

* **If `foundry model list` succeeds**, then:

  * Both local and catalog paths are healthy on VPN
  * We will proceed to a clean **runbook** covering:

    * Service lifecycle
    * Cache paths
    * Ports in use
    * Proxy and TLS requirements

Use this output as the baseline trace for a stable, supportable Foundry Local setup.

