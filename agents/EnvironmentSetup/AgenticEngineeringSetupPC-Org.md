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
5. Install Cursor IDE:  https://cursor.com/download  
   1. Setup an account (if you don't have one. It is free)
   2. As a minimum install the following extensions -> Open extensions (View >> extensions)  
      1. Search for python, and when the results show, click on the ms-python one, and Install it if not already installed  
      2. Search for jupyter, and when the results show, click on the Microsoft one, and Install it if not already installed
   3. Connect to GitHub Repository:
      1. Click on the Source Control icon in the left sidebar (or press Ctrl+Shift+G)
      2. Click on "Clone Repository" button
      3. Select "Clone from GitHub" (you may be prompted to sign in to GitHub)
      4. Authorise Cursor to access your GitHub account when prompted
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
     (Replace `<your-artifactory-url>` with your organisation's Artifactory URL). 
   - This ensures all Python packages come from the MBS approved repository for production deployments

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
1. Configure pip to use organisation's Artifactory repository (MBS approved repository required for production deployments) 

---

## Free API Alternatives (With Limitations)

While the setup above uses OpenAI's paid API service, there are several free alternatives you can explore for experimentation and learning purposes. These options have limitations but are great for getting started:

### 1. **OpenAI Free Tier / Trial Credits**
   - **What it is**: OpenAI often provides free trial credits for new accounts
   - **Limitations**: 
     - Limited to a specific amount of credits (typically $5-18 worth)
     - Credits expire after a certain period
     - Rate limits apply
   - **How to use**: Sign up at https://platform.openai.com/ and check if trial credits are available
   - **Best for**: Initial experimentation and testing

### 2. **Ollama (Local AI Models)**
   - **What it is**: Run large language models locally on your PC
   - **Limitations**: 
     - Requires significant RAM (8GB+ recommended, 16GB+ for larger models)
     - Slower than cloud APIs (depends on your hardware)
     - Limited to models that fit in your system memory
   - **How to use**: 
     - Download from https://ollama.ai/
     - Install and run models like `ollama run llama2`, `ollama run mistral`, etc.
     - Use the local API endpoint instead of OpenAI's API
   - **Best for**: Privacy-sensitive projects, offline development, learning how models work

### 3. **Hugging Face Inference API (Free Tier)**
   - **What it is**: Free access to various AI models via Hugging Face's API
   - **Limitations**: 
     - Rate limited (typically 1,000 requests/month on free tier)
     - Slower response times compared to paid services
     - Some advanced models may not be available on free tier
   - **How to use**: 
     - Sign up at https://huggingface.co/
     - Get your API token from settings
     - Use their Inference API endpoints
   - **Best for**: Experimenting with different models, research projects

### 4. **Google Colab (Free GPU Access)**
   - **What it is**: Free Jupyter notebook environment with GPU access
   - **Limitations**: 
     - Limited GPU hours per day/week
     - Sessions timeout after inactivity
     - Not suitable for production applications
     - Requires Google account
   - **How to use**: 
     - Visit https://colab.research.google.com/
     - Create a new notebook
     - Use free GPU runtime to run models
   - **Best for**: Running experiments, training small models, learning

### 5. **LM Studio (Local Models with UI)**
   - **What it is**: User-friendly desktop application to run LLMs locally
   - **Limitations**: 
     - Same hardware requirements as Ollama
     - Performance depends on your CPU/GPU
     - Model download sizes can be large (several GB)
   - **How to use**: 
     - Download from https://lmstudio.ai/
     - Install and download models through the UI
     - Use the local server API
   - **Best for**: Beginners who want a GUI, local development

### 6. **Groq (Free Tier)**
   - **What it is**: Fast inference API with free tier access
   - **Limitations**: 
     - Rate limits on free tier
     - Limited requests per minute/day
     - May require waitlist or approval
   - **How to use**: 
     - Sign up at https://groq.com/
     - Get API key from dashboard
     - Use similar to OpenAI API
   - **Best for**: Fast inference needs, testing high-throughput scenarios

### 7. **Together AI (Free Tier)**
   - **What it is**: Open-source model inference API
   - **Limitations**: 
     - Free tier has usage limits
     - Rate limits apply
   - **How to use**: 
     - Sign up at https://together.ai/
     - Get API key and use their endpoints
   - **Best for**: Access to open-source models like Llama, Mistral

### 8. **Replicate (Free Tier)**
   - **What it is**: Run AI models in the cloud with free credits
   - **Limitations**: 
     - Limited free credits per month
     - Pay-as-you-go after free tier
   - **How to use**: 
     - Sign up at https://replicate.com/
     - Use their API to run various models
   - **Best for**: Trying different models without local setup

### Recommendations:
- **For absolute beginners**: Start with OpenAI's free trial credits or Hugging Face Inference API
- **For privacy/offline work**: Use Ollama or LM Studio for local models
- **For experimentation**: Try Google Colab for GPU-accelerated experiments
- **For production-like testing**: Use Groq or Together AI free tiers for faster inference