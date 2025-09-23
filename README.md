# AI-Powered Choose Your Own Adventure

A comprehensive 3-day Python programming course for children aged 9-11, teaching fundamental programming concepts through an interactive, AI-enhanced adventure game. This educational project guides young learners through a carefully structured journey from basic Python programming to building complete applications with AI integration.

> **📌 Important**: This repository uses different branches for each day of the course. The `main` branch contains the complete project. Students should start with `session/01` for Day 1. See [Project Structure](#-project-structure---daily-branches) below for details.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [🎯 Learning Objectives](#%F0%9F%8E%AF-learning-objectives)
- [What Students Will Build](#what-students-will-build)
- [Course Philosophy](#course-philosophy)
- [📋 Prerequisites](#%F0%9F%93%8B-prerequisites)
- [🚀 Complete Installation Guide](#%F0%9F%9A%80-complete-installation-guide)
- [Step 1: Python Installation](#step-1-python-installation)
  * [1.1 Pre-Installation Check](#11-pre-installation-check)
    + [Windows](#windows)
    + [macOS](#macos)
    + [Raspberry Pi](#raspberry-pi)
  * [1.2 Installation Instructions](#12-installation-instructions)
    + [Windows Installation](#windows-installation)
    + [macOS Installation](#macos-installation)
    + [Raspberry Pi Installation](#raspberry-pi-installation)
  * [1.3 Post-Installation Verification](#13-post-installation-verification)
    + [Windows](#windows-1)
    + [macOS](#macos-1)
    + [Raspberry Pi](#raspberry-pi-1)
  * [1.4 Troubleshooting Python](#14-troubleshooting-python)
- [Step 2: Git Installation](#step-2-git-installation)
  * [2.1 Pre-Installation Check](#21-pre-installation-check)
    + [All Platforms](#all-platforms)
  * [2.2 Installation Instructions](#22-installation-instructions)
    + [Windows Installation](#windows-installation-1)
    + [macOS Installation](#macos-installation-1)
    + [Raspberry Pi Installation](#raspberry-pi-installation-1)
  * [2.3 Post-Installation Verification](#23-post-installation-verification)
  * [2.4 Troubleshooting Git](#24-troubleshooting-git)
- [Step 3: Visual Studio Code Installation](#step-3-visual-studio-code-installation)
  * [3.1 Pre-Installation Check](#31-pre-installation-check)
    + [All Platforms](#all-platforms-1)
  * [3.2 Installation Instructions](#32-installation-instructions)
    + [Windows Installation](#windows-installation-2)
    + [macOS Installation](#macos-installation-2)
    + [Raspberry Pi Installation](#raspberry-pi-installation-2)
  * [3.3 Post-Installation Verification](#33-post-installation-verification)
  * [3.4 Troubleshooting VS Code](#34-troubleshooting-vs-code)
- [Step 4: Python Extension for VS Code](#step-4-python-extension-for-vs-code)
  * [4.1 Pre-Installation Check](#41-pre-installation-check)
  * [4.2 Installation Instructions](#42-installation-instructions)
  * [4.3 Post-Installation Verification](#43-post-installation-verification)
  * [4.4 Troubleshooting Python Extension](#44-troubleshooting-python-extension)
- [Step 5: Clone the Project](#step-5-clone-the-project)
  * [5.1 Pre-Setup Check](#51-pre-setup-check)
  * [5.2 Clone Instructions](#52-clone-instructions)
    + [Windows](#windows-2)
    + [macOS/Raspberry Pi](#macosraspberry-pi)
  * [5.3 Post-Clone Verification](#53-post-clone-verification)
  * [5.4 Troubleshooting Cloning](#54-troubleshooting-cloning)
- [Step 6: Create Virtual Environment](#step-6-create-virtual-environment)
  * [6.1 Pre-Setup Check](#61-pre-setup-check)
  * [6.2 Create Virtual Environment](#62-create-virtual-environment)
    + [Windows](#windows-3)
    + [macOS/Raspberry Pi](#macosraspberry-pi-1)
  * [6.3 Post-Setup Verification](#63-post-setup-verification)
  * [6.4 Troubleshooting Virtual Environment](#64-troubleshooting-virtual-environment)
- [Step 7: Install Python Dependencies](#step-7-install-python-dependencies)
  * [7.1 Pre-Installation Check](#71-pre-installation-check)
  * [7.2 Installation](#72-installation)
  * [7.3 Post-Installation Verification](#73-post-installation-verification)
  * [7.4 Troubleshooting Dependencies](#74-troubleshooting-dependencies)
- [Step 8: Session Management](#step-8-session-management)
  * [8.1 Understanding the Session System](#81-understanding-the-session-system)
  * [8.2 Using the Session Loader](#82-using-the-session-loader)
  * [8.3 How to Use the Session Loader](#83-how-to-use-the-session-loader)
  * [8.4 Session Structure](#84-session-structure)
  * [8.5 Backup System](#85-backup-system)
  * [8.6 Best Practices](#86-best-practices)
- [Step 9: Ollama Installation (Optional)](#step-9-ollama-installation-optional)
  * [9.1 Pre-Installation Check](#91-pre-installation-check)
  * [9.2 Installation Instructions](#92-installation-instructions)
    + [Windows Installation](#windows-installation-3)
    + [macOS Installation](#macos-installation-3)
    + [Raspberry Pi Installation](#raspberry-pi-installation-3)
  * [9.3 Download Model](#93-download-model)
  * [9.4 Post-Installation Verification](#94-post-installation-verification)
  * [9.5 Troubleshooting Ollama](#95-troubleshooting-ollama)
- [Step 10: Configure for Network Ollama (If Provided by Instructor)](#step-10-configure-for-network-ollama-if-provided-by-instructor)
  * [10.1 Configuration](#101-configuration)
  * [10.2 Test Network Connection](#102-test-network-connection)
- [🎮 Running the Adventure](#%F0%9F%8E%AE-running-the-adventure)
  * [Final Setup Verification](#final-setup-verification)
  * [Run the Game](#run-the-game)
- [📚 Quick Reference](#%F0%9F%93%9A-quick-reference)
  * [Common Commands](#common-commands)
  * [File Locations](#file-locations)
- [🆘 Getting Help](#%F0%9F%86%98-getting-help)
- [📄 License](#%F0%9F%93%84-license)

## 🎯 Learning Objectives

### Learning Progression

**Day 1: Foundation & Setup**
- Environment setup with Python 3.11+ and virtual environments
- Basic programming primitives (strings, numbers, variables)
- Input/output operations and user interaction
- Simple decision making with if-else statements
- Basic loops and repetition

**Day 2: Core Programming Concepts**
- Advanced decision making and logical operations
- Function creation and parameter handling
- Introduction to AI integration concepts
- Code organization and structure

**Day 3: Complete Application Development**
- File-based data management
- Complex game mechanics and state management
- AI API integration with fallback systems
- Final project completion and personalization

### Technical Skills Acquired

- **Introduction to Python Programming**: Variables, functions, conditionals, and loops
- **AI Integration**: Understanding how to interact with AI models safely with fallbacks
- **Data Management**: Reading and writing configuration files
- **Game Design**: Story structure, player choices, and state management
- **Problem Solving**: Debugging and iterative development
- **Network Programming**: HTTP requests and API communication

## What Students Will Build

### The Enchanted Forest Adventure

Students create an interactive text-based adventure game featuring:

- **Dynamic storytelling** powered by AI (with reliable fallbacks)
- **Inventory management** and item collection mechanics
- **Puzzle-solving elements** requiring logical thinking
- **Multiple story paths** leading to different outcomes
- **Personalized content** adapted to individual player choices

### Key Programming Concepts Learned

1. **Data Types and Variables**: Strings, numbers, booleans, and lists
2. **Control Flow**: Decision making and loops for game logic
3. **Functions**: Organizing code into reusable components
4. **File Operations**: Reading configuration and story data
5. **API Integration**: Connecting to AI services with error handling
6. **User Interface**: Creating engaging command-line interactions

## Course Philosophy

### Child-Friendly Learning Approach

- **Visual metaphors** and familiar analogies (LEGO blocks, conversations)
- **Australian context** with relatable examples and encouraging language
- **Immediate feedback** through interactive programs and visible results
- **Progressive complexity** building confidence with each success

### Hands-On Discovery Method

- **Show first**: Demonstrate working code before explaining theory
- **Modify second**: Let students change working code to see effects
- **Create third**: Build new features once concepts are understood
- **Break things safely**: Encourage experimentation and learning from errors

### Educational Outcomes

By completing this course, students will:

- Understand fundamental programming concepts applicable to any language
- Have experience with real-world development tools and practices
- Feel confident about their ability to create functional applications
- Possess a personalized game they built and can share with friends
- Be prepared for advanced programming concepts and continued learning

This course transforms complete beginners into young programmers who understand how software works and feel excited about creating their own digital projects.

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

## Step 8: Session Management

### 8.1 Understanding the Session System

This project includes a session management system that allows you to switch between different course days or development stages. Each session represents a complete state of the project at a specific point in the course.

### 8.2 Using the Session Loader

The `load_session.sh` script helps you:
1. **Backup your current work** - Creates a timestamped backup of your current `src` directory
2. **Switch to a specific session** - Loads the code for a particular course day
3. **Preserve your progress** - Ensures no work is lost when switching sessions

### 8.3 How to Use the Session Loader

1. **Make the script executable** (first time only):
   ```bash
   chmod +x load_session.sh
   ```

2. **Run the session loader**:
   ```bash
   ./load_session.sh
   ```

3. **Select your desired session**:
   The script will show available sessions:
   ```
   What session would you like to load?
   
   1. Session 1
   2. Session 2
   3. Session 3
   4. Session 4
   5. Session 5
   
   Enter your choice (1-5):
   ```

4. **Confirm the operation**:
   The script will:
   - Create a backup: `backup/src-2025-09-13-04-27-20-pm.tar.gz`
   - Clear the current `src` directory
   - Load the selected session code into `src`

### 8.4 Session Structure

The course uses a session-based approach where each learning module is contained in its own session folder:

```
session/1/    # Module 1 - Programming Primitives
session/2/    # Module 2 - Functions and Organization
session/3/    # Module 3 - AI Integration Basics
session/4/    # Module 4 - File Operations and Data
session/5/    # Module 5 - Complete AI-Powered Game
```

**Session 1: Programming Primitives and Fundamentals**
- Introduction to Python programming fundamentals
- Basic data types (strings, numbers, booleans)
- Input/output operations and user interaction
- Simple decision making with if-else statements
- Basic loops and repetition
- File: `hello-world.py`, `primitives-demo.py`, `input-output-demo.py`, `if-else-demo.py`, `loops-demo.py`

**Session 2: Functions and Organization**
- Understanding what functions are and how to create them
- Function parameters and return values
- Code organization and program structure
- The `if __name__ == "__main__"` pattern
- File: `main.py` (focus on functions)

**Session 3: AI Integration Basics**
- HTTP API calls to external AI systems (Ollama)
- Handling network errors gracefully
- Building robust applications with AI services
- Master Oogway character interaction demo
- Files: `main.py` (AI integration), `test-ollama.py`

**Session 4: File Operations and Data Management**
- Reading and processing data from external files
- Using Python's `configparser` library
- Creating data-driven applications
- Separating game logic from content
- Files: `main.py`, `data.ini`, `stories.ini`, `write-file.py`, `path-finder.py`

**Session 5: Complete AI-Powered Adventure Game**
- Integrating AI services with robust fallback mechanisms
- Dynamic, personalized story generation
- Game mechanics: inventory, path resolution, choice handling
- Complete application architecture
- Error handling and resilience

### 8.5 Backup System

Your work is automatically backed up to the `backup/` directory with timestamps:
- Format: `src-YYYY-MM-DD-HH-MM-SS-am/pm.tar.gz`
- Example: `src-2025-09-13-04-27-20-pm.tar.gz`

To restore from a backup:
```bash
cd src
tar -xzf ../backup/src-2025-09-13-04-27-20-pm.tar.gz
```

### 8.6 Best Practices

- **Always use the session loader** instead of manually copying files
- **Run the script from the project root directory**
- **Your backups are preserved** - you can always restore previous work
- **Start each day with the appropriate session** for the course

---

## Step 9: Ollama Installation (Optional)

### 9.1 Pre-Installation Check

```bash
ollama --version
```
**If you see version info, check models:**
```bash
ollama list
```
**If "llama3.2" is listed, skip to Step 9 ✅**

### 9.2 Installation Instructions

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

### 9.3 Download Model

```bash
ollama pull llama3.2
```
This downloads ~2GB, may take 5-10 minutes.

### 9.4 Post-Installation Verification

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

### 9.5 Troubleshooting Ollama

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

## Step 10: Configure for Network Ollama (If Provided by Instructor)

### 10.1 Configuration

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

### 10.2 Test Network Connection

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

This project is for educational purposes. [MIT License.](LICENSE)