# AI-Powered Choose Your Own Adventure

An educational Python project that teaches young students (Years 3-5) the basics of computer science through interactive storytelling powered by AI.

> **📌 Important**: This repository uses different branches for each day of the course. The `main` branch contains the complete project. Students should start with `session/01` for Day 1. See [Project Structure](#-project-structure---daily-branches) below for details.

## 🎯 Learning Objectives

- **Introduction to Python Programming**: Variables, functions, conditionals, and loops
- **GUI Development**: Working with Tkinter for desktop applications  
- **AI Integration**: Understanding how to interact with AI models
- **Game Design**: Story structure, player choices, and state management
- **Problem Solving**: Debugging and iterative development

## 📋 Prerequisites

- Computer with Windows 10/11, macOS 10.14+, or Raspberry Pi OS
- Internet connection for initial setup
- About 4GB of free disk space
- Basic keyboard and mouse skills

## 🚀 Complete Installation Guide

We'll install each component step-by-step. For each tool, we'll:
1. Check if it's already installed
2. Install it if needed
3. Verify it's working
4. Fix any problems

---

## Step 1: Python Installation

### 1.1 Pre-Installation Check

#### Windows
Open Command Prompt (Win+R, type `cmd`, press Enter) and run:
```cmd
python --version
```
**Expected Result:** `Python 3.11.x` or newer
**If you see this, skip to Step 2 ✅**

#### macOS
Open Terminal (Cmd+Space, type "Terminal", press Enter) and run:
```bash
python3 --version
```
**Expected Result:** `Python 3.11.x` or newer
**If you see this, skip to Step 2 ✅**

#### Raspberry Pi
Open Terminal and run:
```bash
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"
```
**Expected Result:** Python 3.9+ and "Tkinter OK"
**If both work, skip to Step 2 ✅**

### 1.2 Installation Instructions

#### Windows Installation
1. Visit https://www.python.org/downloads/
2. Click the yellow "Download Python 3.11.x" button
3. Run the downloaded installer
4. **CRITICAL**: ✅ Check "Add Python to PATH" at the bottom
5. Click "Install Now"
6. When complete, click "Close"

#### macOS Installation
1. First install Homebrew (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python:
   ```bash
   brew install python@3.11
   ```

#### Raspberry Pi Installation
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-tk -y
```

### 1.3 Post-Installation Verification

#### Windows
Open a **NEW** Command Prompt and run:
```cmd
python --version
pip --version
python -c "import tkinter; print('Tkinter OK')"
```

#### macOS
```bash
python3 --version
python3 -m pip --version
python3 -c "import tkinter; print('Tkinter OK')"
```

#### Raspberry Pi
```bash
python3 --version
python3 -m pip --version
python3 -c "import tkinter; print('Tkinter OK')"
```

### 1.4 Troubleshooting Python

**Problem: "python is not recognized" (Windows)**
- Solution: Python wasn't added to PATH
- Fix: Uninstall Python, reinstall with "Add to PATH" checked
- Alternative: Use `py` instead of `python`

**Problem: "command not found" (Mac/Linux)**
- Solution: Use `python3` instead of `python`
- Fix: Create alias: `echo "alias python=python3" >> ~/.bashrc`

**Problem: "No module named tkinter"**
- Windows: Reinstall Python with default options
- macOS: `brew install python-tk`
- Raspberry Pi: `sudo apt-get install python3-tk`

**Problem: pip not found**
- Windows: `python -m ensurepip --upgrade`
- macOS/Linux: `python3 -m ensurepip --upgrade`

---

## Step 2: Git Installation

### 2.1 Pre-Installation Check

#### All Platforms
Run in your terminal/command prompt:
```bash
git --version
```
**Expected Result:** `git version 2.x.x`
**If you see this, skip to Step 3 ✅**

### 2.2 Installation Instructions

#### Windows Installation
1. Visit https://git-scm.com/download/win
2. Download the 64-bit installer
3. Run the installer
4. Use all default settings (just keep clicking "Next")
5. Click "Install" then "Finish"

#### macOS Installation
Option 1 - Via Homebrew:
```bash
brew install git
```

Option 2 - Via Xcode:
```bash
xcode-select --install
```

#### Raspberry Pi Installation
```bash
sudo apt install git -y
```

### 2.3 Post-Installation Verification

Open a **NEW** terminal/command prompt:
```bash
git --version
git config --global user.name
```

If user.name is empty, configure Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2.4 Troubleshooting Git

**Problem: "git is not recognized" (Windows)**
- Solution: Close and reopen Command Prompt
- Fix: Add Git to PATH manually:
  - Search "Environment Variables" in Start Menu
  - Add `C:\Program Files\Git\bin` to PATH

**Problem: SSL certificate error**
- Temporary fix: `git config --global http.sslVerify false`
- Note: Only use on trusted networks

**Problem: Permission denied (Mac/Linux)**
- Fix: `sudo` before the command
- Better: Fix permissions: `sudo chown -R $(whoami) ~/.config`

---

## Step 3: Visual Studio Code Installation

### 3.1 Pre-Installation Check

#### All Platforms
```bash
code --version
```
**Expected Result:** Version information
**If you see this, skip to Step 4 ✅**

Alternative check: Look for "Visual Studio Code" in:
- Windows: Start Menu
- macOS: Applications folder
- Linux: Applications menu

### 3.2 Installation Instructions

#### Windows Installation
1. Visit https://code.visualstudio.com/
2. Click "Download for Windows"
3. Run the installer
4. **IMPORTANT** - Check these boxes:
   - ✅ Add to PATH (required)
   - ✅ Create desktop icon
   - ✅ Add "Open with Code" to context menu
   - ✅ Register Code as editor for supported files
5. Click "Next" then "Install"

#### macOS Installation
1. Visit https://code.visualstudio.com/
2. Click "Download for Mac"
3. Open the downloaded .zip file
4. Drag Visual Studio Code to Applications folder
5. Open VS Code from Applications
6. Enable command line:
   - Press Cmd+Shift+P
   - Type "shell command"
   - Select "Install 'code' command in PATH"

#### Raspberry Pi Installation
For 64-bit Raspberry Pi OS:
```bash
sudo apt update
sudo apt install code -y
```

For 32-bit Raspberry Pi OS:
```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y
```

### 3.3 Post-Installation Verification

1. Open a **NEW** terminal/command prompt:
   ```bash
   code --version
   ```

2. Test VS Code opens:
   ```bash
   code .
   ```
   VS Code should open showing the current folder

### 3.4 Troubleshooting VS Code

**Problem: "code is not recognized" (Windows)**
- Solution: Restart computer
- Alternative: Full path: `"C:\Program Files\Microsoft VS Code\bin\code"`

**Problem: "code: command not found" (Mac)**
- Fix: In VS Code, press Cmd+Shift+P → "Install 'code' command"

**Problem: VS Code won't open (Linux)**
- Check: `which code`
- Fix permissions: `sudo chmod +x /usr/bin/code`

**Problem: Extensions not working**
- Fix: View → Extensions → Search "Python" → Install/Reinstall

---

## Step 4: Python Extension for VS Code

### 4.1 Pre-Installation Check

1. Open VS Code
2. Press Ctrl+Shift+X (Cmd+Shift+X on Mac)
3. Search for "Python"
4. Look for "Python" by Microsoft

**If it shows "Installed", skip to Step 5 ✅**

### 4.2 Installation Instructions

1. In VS Code Extensions panel (Ctrl+Shift+X):
2. Search: "Python"
3. Find "Python" by Microsoft (usually first result)
4. Click "Install"
5. Wait for "Installing..." to complete
6. Reload VS Code if prompted

### 4.3 Post-Installation Verification

1. Create a test file:
   - Press Ctrl+N (Cmd+N on Mac)
   - Save as `test.py`
   - Type: `print("Hello World")`

2. Check for:
   - Syntax highlighting (colors in code)
   - "Python" shown in bottom status bar
   - Run button (▶️) in top right

3. Run the test:
   - Click the Run button OR
   - Press Ctrl+F5 (Cmd+F5 on Mac)

### 4.4 Troubleshooting Python Extension

**Problem: No syntax highlighting**
- Fix: Click "Plain Text" in bottom right → Select "Python"

**Problem: "Select Python Interpreter" message**
- Fix: Click it → Select Python 3.11

**Problem: Can't run Python files**
- Fix: Reinstall extension
- Alternative: Terminal → `python test.py`

---

## Step 5: Clone the Project

### 5.1 Pre-Setup Check

Ensure you have:
- ✅ Git installed (Step 2)
- ✅ A folder for your projects

### 5.2 Clone Instructions

#### Windows
```cmd
cd %USERPROFILE%
mkdir Projects
cd Projects
git clone https://github.com/psenger/ai-powered-choose-your-own-adventure.git
cd ai-powered-choose-your-own-adventure
```

#### macOS/Raspberry Pi
```bash
cd ~
mkdir -p Projects
cd Projects
git clone https://github.com/psenger/ai-powered-choose-your-own-adventure.git
cd ai-powered-choose-your-own-adventure
```

### 5.3 Post-Clone Verification

```bash
ls -la
```
You should see files like:
- main.py
- README.md
- config.py

### 5.4 Troubleshooting Cloning

**Problem: "Permission denied (publickey)"**
- Fix: Use HTTPS instead:
  ```bash
  git clone https://github.com/psenger/ai-powered-choose-your-own-adventure.git
  ```

**Problem: "Repository not found"**
- Check URL spelling
- Ensure repository is public

**Problem: "Could not resolve host"**
- Check internet connection
- Try: `ping github.com`

---

## Step 6: Create Virtual Environment

### 6.1 Pre-Setup Check

Ensure you're in the project directory:
```bash
pwd
```
Should end with: `/ai-powered-choose-your-own-adventure`

### 6.2 Create Virtual Environment

> **Note**: We use `venv` (not `.venv` with a dot) so the folder is visible to students. Both names work and are ignored by git.

#### Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

#### macOS/Raspberry Pi
```bash
python3 -m venv venv
source venv/bin/activate
```

### 6.3 Post-Setup Verification

Your prompt should now show `(venv)` at the beginning.

Test with:
```bash
which python       # Mac/Linux
where python       # Windows
```
Should show a path inside your project's venv folder.

### 6.4 Troubleshooting Virtual Environment

**Problem: "venv is not a valid command"**
- Windows: Use `python -m venv venv`
- Mac/Linux: Use `python3 -m venv venv`

**Problem: "cannot activate"**
- Windows PowerShell: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then: `.\venv\Scripts\Activate.ps1`

**Problem: (venv) not showing**
- Verify: `echo $VIRTUAL_ENV` (Mac/Linux) or `echo %VIRTUAL_ENV%` (Windows)
- Deactivate and reactivate: `deactivate` then activate again

---

## Step 7: Install Python Dependencies

### 7.1 Pre-Installation Check

Ensure:
1. Virtual environment is active (see `(venv)` in prompt)
2. You're in project directory

### 7.2 Installation

```bash
pip install requests
```

Note: tkinter comes with Python, no separate install needed.

### 7.3 Post-Installation Verification

```bash
pip list
```
Should show:
- requests (version 2.x.x)

Test imports:
```bash
python -c "import requests; print('requests OK')"
python -c "import tkinter; print('tkinter OK')"
```

### 7.4 Troubleshooting Dependencies

**Problem: "pip: command not found"**
- Use: `python -m pip install requests`

**Problem: "No module named tkinter"**
- Windows: Reinstall Python with defaults
- macOS: `brew install python-tk`
- Linux: `sudo apt-get install python3-tk`

**Problem: SSL Certificate error**
- Fix: `pip install --trusted-host pypi.org requests`

---

## Step 8: Ollama Installation (Optional)

### 8.1 Pre-Installation Check

```bash
ollama --version
```
**If you see version info, check models:**
```bash
ollama list
```
**If "llama3.2" is listed, skip to Step 9 ✅**

### 8.2 Installation Instructions

#### Windows Installation
1. Visit https://ollama.com/download/windows
2. Download OllamaSetup.exe
3. Run installer (Administrator rights required)
4. Follow installation wizard

#### macOS Installation
1. Visit https://ollama.com/download/mac
2. Download Ollama-darwin.zip
3. Unzip and move to Applications
4. Open Ollama from Applications

#### Raspberry Pi Installation
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 8.3 Download Model

```bash
ollama pull llama3.2
```
This downloads ~2GB, may take 5-10 minutes.

### 8.4 Post-Installation Verification

1. Check Ollama running:
   ```bash
   ollama list
   ```
   Should show llama3.2 model

2. Test model:
   ```bash
   ollama run llama3.2 "Hello"
   ```
   Press Ctrl+D to exit

### 8.5 Troubleshooting Ollama

**Problem: "ollama: command not found"**
- Windows: Restart computer
- Mac: Check Applications folder
- Linux: Add to PATH: `export PATH=$PATH:/usr/local/bin`

**Problem: "Failed to connect"**
- Start Ollama service:
  - Windows: Check system tray
  - Mac: Open Ollama app
  - Linux: `ollama serve`

**Problem: Model download fails**
- Check disk space (need 4GB free)
- Check internet connection
- Try smaller model: `ollama pull tinyllama`

---

## Step 9: Configure for Network Ollama (If Provided by Instructor)

### 9.1 Configuration

If instructor provides network Ollama:

1. Open `config.py` in VS Code
2. Change:
   ```python
   OLLAMA_URL = "http://localhost:11434"
   ```
   To:
   ```python
   OLLAMA_URL = "http://[instructor-ip]:11434"
   ```

### 9.2 Test Network Connection

```python
import requests
response = requests.get("http://[instructor-ip]:11434/api/tags")
print(response.status_code)  # Should print 200
```

---

## 🎮 Running the Adventure

### Final Setup Verification

Save this as `verify_all.py` and run it:

```python
#!/usr/bin/env python3
import sys
import subprocess
import importlib

print("=" * 60)
print("FINAL ENVIRONMENT CHECK")
print("=" * 60)

# Check Python
print(f"Python Version: {sys.version}")
if sys.version_info >= (3, 9):
    print("✅ Python version OK")
else:
    print("❌ Need Python 3.9+")

# Check modules
for module in ['tkinter', 'requests']:
    try:
        importlib.import_module(module)
        print(f"✅ {module} installed")
    except ImportError:
        print(f"❌ {module} NOT installed")

# Check Git
try:
    subprocess.run(["git", "--version"], capture_output=True, check=True)
    print("✅ Git installed")
except:
    print("⚠️  Git not found (optional)")

# Check VS Code
try:
    subprocess.run(["code", "--version"], capture_output=True, check=True)
    print("✅ VS Code installed")
except:
    print("⚠️  VS Code not found (optional)")

# Check Ollama
try:
    subprocess.run(["ollama", "--version"], capture_output=True, check=True)
    print("✅ Ollama installed")
    
    # Check for model
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    if "llama3.2" in result.stdout:
        print("✅ llama3.2 model ready")
    else:
        print("⚠️  Run: ollama pull llama3.2")
except:
    print("⚠️  Ollama not found (optional)")

print("=" * 60)
print("If all critical items show ✅, you're ready to code!")
print("=" * 60)
```

### Run the Game

1. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

2. Run the adventure:
   ```bash
   python main.py
   ```

---

## 📚 Quick Reference

### Common Commands

| Task | Windows | Mac/Linux |
|------|---------|-----------|
| Check Python | `python --version` | `python3 --version` |
| Activate venv | `venv\Scripts\activate` | `source venv/bin/activate` |
| Install package | `pip install [name]` | `pip install [name]` |
| Run program | `python main.py` | `python3 main.py` |
| Deactivate venv | `deactivate` | `deactivate` |

### File Locations

- **Project**: `~/Projects/ai-powered-choose-your-own-adventure`
- **Virtual Environment**: `[project]/venv`
- **Main Game File**: `main.py`
- **Configuration**: `config.py`

---

## 🆘 Getting Help

1. **First**: Check the troubleshooting section for your error
2. **Second**: Try the verify scripts to identify issues
3. **Third**: Ask your instructor
4. **Last Resort**: Google the exact error message

## 📄 License

This project is for educational purposes. MIT License.