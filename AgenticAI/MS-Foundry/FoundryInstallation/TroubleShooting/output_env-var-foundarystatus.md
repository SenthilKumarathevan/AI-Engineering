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
