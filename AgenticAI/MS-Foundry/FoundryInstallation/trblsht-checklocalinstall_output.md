PS C:\Users\P432852> netsh winhttp show proxy

Current WinHTTP proxy settings:

    Direct access (no proxy server).

PS C:\Users\P432852> "`n---`n"

---

PS C:\Users\P432852> Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' |
>>   Select-Object ProxyEnable, ProxyServer, ProxyOverride, AutoConfigURL

ProxyEnable ProxyServer ProxyOverride AutoConfigURL
----------- ----------- ------------- -------------
          0


PS C:\Users\P432852>
PS C:\Users\P432852> "`n---`n"

---

PS C:\Users\P432852>
PS C:\Users\P432852> # 2) Attempt a simple HTTPS fetch and show status + content-type + first 200 chars
PS C:\Users\P432852> $resp = Invoke-WebRequest -Uri "https://example.com" -MaximumRedirection 0 -ErrorAction SilentlyContinue

Security Warning: Script Execution Risk
Invoke-WebRequest parses the content of the web page. Script code in the web page might be run when the page is parsed.
      RECOMMENDED ACTION:
      Use the -UseBasicParsing switch to avoid script code execution.

      Do you want to continue?

[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): a
PS C:\Users\P432852> if ($resp) {
>>   "example.com status: $($resp.StatusCode)"
>>   "example.com content-type: $($resp.Headers.'Content-Type')"
>>   "example.com first200: " + ($resp.Content.Substring(0,[Math]::Min(200,$resp.Content.Length)) -replace "`r|`n"," ")
>> } else {
>>   "example.com request failed: $($Error[0].Exception.Message)"
>> }
example.com status: 200
example.com content-type: text/html
example.com first200: <!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-famil
PS C:\Users\P432852>
PS C:\Users\P432852> "`n---`n"

---

PS C:\Users\P432852>
PS C:\Users\P432852> # 3) Find the Foundry CLI binary actually being executed
PS C:\Users\P432852> Get-Command foundry | Format-List *


HelpUri            :
FileVersionInfo    : File:             C:\Users\P432852\AppData\Local\Microsoft\WindowsApps\foundry.exe
                     InternalName:
                     OriginalFilename:
                     FileVersion:
                     FileDescription:
                     Product:
                     ProductVersion:
                     Debug:            False
                     Patched:          False
                     PreRelease:       False
                     PrivateBuild:     False
                     SpecialBuild:     False
                     Language:

Path               : C:\Users\P432852\AppData\Local\Microsoft\WindowsApps\foundry.exe
Extension          : .exe
Definition         : C:\Users\P432852\AppData\Local\Microsoft\WindowsApps\foundry.exe
Source             : C:\Users\P432852\AppData\Local\Microsoft\WindowsApps\foundry.exe
Version            : 0.0.0.0
Visibility         : Public
OutputType         : {System.String}
Name               : foundry.exe
CommandType        : Application
ModuleName         :
Module             :
RemotingCapability : PowerShell
Parameters         :
ParameterSets      :
