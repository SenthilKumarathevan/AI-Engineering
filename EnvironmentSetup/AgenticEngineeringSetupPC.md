# Setup instructions for PC 

1. Change your permissions to an elevated role, if you have permissions issues when doing the below steps. Or simply run as adminstrator when needing to install the necessary s/w.
2. To see if you have administrative privileges, try using commands like net user %USERNAME% or whoami /groups to see if you are part of the Administrators group. 
3. Remove any limit on windows 260 character filename sizes. 
For an automated fix, run the following PowerShell command as Administrator: 
i. Press Win + R, type regedit, and press Enter. 
ii. Navigate to:
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
``` 
iii. Find LongPathsEnabled.  
iv. If it doesn’t exist, right-click, choose New → DWORD (32-bit) Value, and name it LongPathsEnabled.  
v. Double-click LongPathsEnabled and set Value data to 1.  
vi. Click OK and restart your computer.   

Or you can do the above change in powershell by opening it as Adminstrator and running the following command:  
```
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -Type DWord
```  
Restart PC to apply changes.  

4. Install Git (if not already installed) https://git-scm.com/download/win  
5. Install Cursor IDE: https://git-scm.com/download/win  
   1. Setup an account (if you don't have one. It is free)
   2. As a minimum install the following extensions -> Open extensions (View >> extensions)  
      1. Search for python, and when the results show, click on the ms-python one, and Install it if not already installed  
      2. Search for jupyter, and when the results show, click on the Microsoft one, and Install it if not already installed
6. Install UV - Recommended to install and use the standalone installer.
   1. https://docs.astral.sh/uv/getting-started/installation/  directly to windows install section: https://docs.astral.sh/uv/#__tabbed_1_2
   2. open a Powershell as Administrator
   3. Copy and paste the ps command to the terminal
   4. Restart all terminal shells you have open, restart cursor / vscode  
   5. To check if it is installed, by ouputting the version ```uv --version```  

7. Now that you you have uv installed you need to use it in the project directory:
   1. run ```uv sync``` to create a .venv folder in the project directory  
   2. notice that a .venv folder has been created in the project directory you ran in from (should be the root of the project folder)  
      1. You can build a requirements.txt file fo you project packages by running the following command from the project root folder at the terminal:  
      ```uv pip compile pyproject.toml -o requirements.txt```  

8. Fund your credit balance and setup your API key with OpenAI:   
   1. login to account:https://platform.openai.com/  
   2. On the portal, click the gear icon top right
   3. on the left pane click Billing, top up your balance as needed, depending expected token usage. (If you don't want to be automatically billed everytime you reach a minumum set threshold, set Auto recharge to off).  
   4. Once you have the desired credit balance, click API keys and generate your key for use with you interface.
      1. Ensure to copy and paste the key to a saved location, as you will not be able to see it again in the portal once closed.
   
9.  Configure the OpenAI API key for use with your project (assuming you already have a OpenAI account and step 8 is completed)  
    1.  In the project root folder create a new file called .env (this will be your environment vars for your project, which includes the key)
    2.  Add the following line to the .env file: ```OPENAI_API_KEY=<your openai api key you copied earlier>```  

This now completes the set up of your Agentic AI Engineering confguration, which incorporates a one time setup of:
1. Windows long filenames enabling
2. Setup of Cursor
3. Setup of UV
4. Set up of OpenAI API key and funding account  

For project specific:#
1. run uv sync to project root to create the projects .venv virtual environment.
2. set up of .env file and add the openai api key configuraton 