# Setup instructions for PC (Example using OpenAI API) 

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
5. Install Cursor IDE:  https://cursor.com/download  
   1. Setup an account (if you don't have one. It is free)
   2. As a minimum install the following extensions -> Open extensions (View >> extensions)  
      1. Search for python, and when the results show, click on the ms-python one, and Install it if not already installed  
      2. Search for jupyter, and when the results show, click on the Microsoft one, and Install it if not already installed
   3. Connect to GitHub Repository:
      1. Click on the Source Control icon in the left sidebar (or press Ctrl+Shift+G)
      2. Click on "Clone Repository" button
      3. Select "Clone from GitHub" (you may be prompted to sign in to GitHub)
      4. Authorize Cursor to access your GitHub account when prompted
      5. A list of repositories accessible to you will appear
      6. Select the repository you want to work with (e.g., AI-Engineering)
      7. Choose a local folder location to clone the repository
      8. Once cloned, click "Open" to open the repository in Cursor

6. Install Python (if not already installed):
   1. Download Python from https://www.python.org/downloads/ (version 3.10 or higher recommended)
   2. During installation, make sure to check "Add Python to PATH"
   3. Verify installation by opening a new PowerShell terminal and running: ```python --version```

7. Set up Python Virtual Environment and Install Dependencies:
   1. Open a PowerShell terminal in Cursor (Terminal >> New Terminal)
   2. Navigate to your project root directory
   3. Create a virtual environment:
      ```
      python -m venv .venv
      ```
   4. Activate the virtual environment:
      ```
      .venv\Scripts\Activate.ps1
      ```
      Note: If you encounter an execution policy error, run: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
   5. Upgrade pip to the latest version:
      ```
      python -m pip install --upgrade pip
      ```
   6. Install project dependencies:
      - If you have a requirements.txt file:
        ```
        pip install -r requirements.txt
        ```
      - If you have a pyproject.toml file, install dependencies using:
        ```
        pip install -e .
        ```
      - Or install specific packages as needed:
        ```
        pip install <package-name>
        ```
   7. To save your current environment's packages to requirements.txt:
      ```
      pip freeze > requirements.txt
      ```  

8. Fund your credit balance and setup your API key with OpenAI:   
   
   **Note**: This example demonstrates setup using the OpenAI API. However, you can use any API that you have access to, as long as you are able to retrieve the API key or set/configure an API key and use it in the configuration.
   
   1. login to account:https://platform.openai.com/  
   2. On the portal, click the gear icon top right
   3. on the left pane click Billing, top up your balance as needed, depending expected token usage. (If you don't want to be automatically billed everytime you reach a minumum set threshold, set Auto recharge to off).  
   4. Once you have the desired credit balance, click API keys and generate your key for use with you interface.
      1. Ensure to copy and paste the key to a saved location, as you will not be able to see it again in the portal once closed.
   
9.  Configure the OpenAI API key for use with your project (assuming you already have a OpenAI account and step 8 is completed)  
    1.  In the project root folder create a new file called .env (this will be your environment vars for your project, which includes the key)
    2.  Add the following line to the .env file: ```OPENAI_API_KEY=<your openai api key you copied earlier>```  

---

## Productionisation Requirements

**Note**: The following steps are **only necessary when productionising code** as Python libraries and packages. For development and experimentation, you can use the standard public PIP repository, which is easier to download from and does not require additional configuration.

### For Productionisation Only:

1. **Configure pip to use the organisation's approved Artifactory repository**:
   - The Artifactory pip repository is required to ensure compliance with MBS (Master Build System) approved repositories when productionising code
   - Configure pip to use Artifactory:
     ```
     pip config set global.index-url https://<your-artifactory-url>/artifactory/api/pypi/pypi-virtual/simple
     ```
     (Replace `<artifactory-url>` with Artifactory URL. See Artifactory documentation for onboarding and setup.)
   - This ensures all Python packages come from the MBS approved repository for production deployments
  
  NB: The use of artifactory for python packages it seems is not being always used, but from a compliance point of view this needs to be determined on how it is enforced.

### For Development and Experimentation:

- **Use the standard public PIP repository**: No additional configuration is needed. The default pip package manager will use the public PyPI repository, which is suitable for development and experimentation purposes.

---

### This now completes the set up of your Agentic AI Engineering configuration, which incorporates a one time setup of:
1. Windows long filenames enabling
2. Git installation
3. Setup of Cursor IDE
4. Connection to GitHub repository
5. Python installation
6. Set up of OpenAI API key and funding account  

### For project specific setup:
1. Create and activate Python virtual environment (.venv) in project root
2. Install project dependencies using pip (uses standard public PIP repository by default for development/experimentation)
3. Set up .env file and add the OpenAI API key configuration

### For productionisation only:
1. Configure pip to use organisation's Artifactory repository (NBS approved repository required for production deployments) 