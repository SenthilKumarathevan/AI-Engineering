### Localhost proxy bypass (important for Foundry Local)

This project relies on a **local HTTP service** (Foundry Local) that listens on
`http://127.0.0.1:<port>`.

On corporate-managed machines, a user-level proxy may be configured that
**incorrectly attempts to proxy localhost traffic**, which breaks communication
between the Foundry CLI / Python SDKs and the local service.

To prevent this, the user’s WinINET proxy bypass list includes: <local>;localhost;127.0.0.1  


This setting:
- Is **user-scoped** (no admin rights required)
- Does **not** disable the corporate proxy for external traffic
- Applies automatically across PowerShell, VS Code terminals, CLI tools, and Python
- Is required for reliable use of:
  - Foundry CLI
  - Foundry Local
  - Python SDKs (`foundry-local`, OpenAI-compatible clients)

If local model listing or inference fails with proxy or DNS-style errors,
verify that localhost is present in the user-level proxy bypass list.

## Why this is the best option for your setup  

* Safest scope: user-level only
* Most reliable: works across shells and tools
* Python-friendly: avoids per-script proxy hacks
* Standard practice for local services in proxy-controlled environments*

## You are now set up correctly for:  

* Foundry CLI usage
* Foundry Local SDK in Python
* Installing and running dependencies without proxy-related surprises
