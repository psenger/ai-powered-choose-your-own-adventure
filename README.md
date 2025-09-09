# AI-Powered Choose Your Own Adventure

An educational Python project that teaches young students (Years 3-5) the basics of computer science through interactive storytelling powered by AI.

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

## 🚀 Installation Guide

### Step 1: Install Python

#### Windows
1. Visit https://www.python.org/downloads/
2. Download Python 3.11 or newer (Click the yellow "Download Python" button)
3. Run the installer
4. **IMPORTANT**: Check ✅ "Add Python to PATH" at the bottom of the installer
5. Click "Install Now"
6. Verify installation:
   - Open Command Prompt (Press Win+R, type `cmd`, press Enter)
   - Type `python --version` and press Enter
   - You should see `Python 3.11.x` or newer

#### macOS
1. Open Terminal (Press Cmd+Space, type "Terminal", press Enter)
2. Install Homebrew if not installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```bash
   brew install python@3.11
   ```
4. Verify installation:
   ```bash
   python3 --version
   ```

#### Raspberry Pi
1. Open Terminal
2. Update your system:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```
3. Install Python and pip:
   ```bash
   sudo apt install python3 python3-pip python3-tk -y
   ```
4. Verify installation:
   ```bash
   python3 --version
   ```

### Step 2: Install Git

#### Windows
1. Visit https://git-scm.com/download/win
2. Download the installer
3. Run the installer (keep all default settings)
4. Verify in Command Prompt:
   ```bash
   git --version
   ```

#### macOS
1. In Terminal:
   ```bash
   brew install git
   ```
2. Verify:
   ```bash
   git --version
   ```

#### Raspberry Pi
1. In Terminal:
   ```bash
   sudo apt install git -y
   ```
2. Verify:
   ```bash
   git --version
   ```

### Step 3: Install Visual Studio Code

#### Windows
1. Visit https://code.visualstudio.com/
2. Click "Download for Windows"
3. Run the installer
4. During installation, check:
   - ✅ "Add to PATH"
   - ✅ "Create Desktop Icon"
   - ✅ "Add to context menu"

#### macOS
1. Visit https://code.visualstudio.com/
2. Click "Download for Mac"
3. Open the downloaded .zip file
4. Drag Visual Studio Code to Applications folder
5. Open VS Code from Applications

#### Raspberry Pi
1. In Terminal:
   ```bash
   sudo apt install code -y
   ```
   Or for older Raspberry Pi:
   ```bash
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
   sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
   sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
   sudo apt update
   sudo apt install code
   ```

### Step 4: Configure VS Code for Python

1. Open Visual Studio Code
2. Click Extensions icon (left sidebar, looks like 4 squares)
3. Search for "Python"
4. Install the official Python extension by Microsoft
5. Restart VS Code

### Step 5: Clone the Project

#### All Platforms
1. Create a projects folder:
   - **Windows**: Open Command Prompt
     ```bash
     cd %USERPROFILE%
     mkdir Projects
     cd Projects
     ```
   - **macOS/Raspberry Pi**: Open Terminal
     ```bash
     cd ~
     mkdir Projects
     cd Projects
     ```

2. Clone the repository:
   ```bash
   git clone https://github.com/psenger/ai-powered-choose-your-own-adventure.git
   ```

3. Enter the project folder:
   ```bash
   cd ai-powered-choose-your-own-adventure
   ```

### Step 6: Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Raspberry Pi
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command line.

### Step 7: Install Project Dependencies

With virtual environment activated:
```bash
pip install requests tkinter
```

Note: tkinter usually comes pre-installed with Python. If you get an error:
- **Windows/Mac**: Reinstall Python and ensure tkinter is included
- **Raspberry Pi**: `sudo apt-get install python3-tk`

### Step 8: Install Ollama (Optional - Instructor May Provide Network Access)

#### Windows
1. Visit https://ollama.com/download/windows
2. Download and run OllamaSetup.exe
3. Open Command Prompt and verify:
   ```bash
   ollama --version
   ```
4. Download a model:
   ```bash
   ollama pull llama3.2
   ```

#### macOS
1. Visit https://ollama.com/download/mac
2. Download and install Ollama
3. Open Terminal and verify:
   ```bash
   ollama --version
   ```
4. Download a model:
   ```bash
   ollama pull llama3.2
   ```

#### Raspberry Pi
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
```

### Step 9: Configure for Network Ollama (If Instructor Provides)

If your instructor is running Ollama on the network:
1. Open `config.py` in VS Code
2. Change the OLLAMA_URL from:
   ```python
   OLLAMA_URL = "http://localhost:11434"
   ```
   To the instructor-provided address:
   ```python
   OLLAMA_URL = "http://instructor-computer-ip:11434"
   ```

## 🎮 Running the Adventure

1. Make sure you're in the project directory
2. Activate virtual environment (if not already active)
3. Run the game:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
ai-powered-choose-your-own-adventure/
│
├── main.py           # Main game file
├── config.py         # Configuration settings
├── situations.py     # Story situations and choices
├── game_gui.py       # GUI interface code
├── ai_storyteller.py # Ollama integration
├── README.md         # This file
└── Claude.md         # Development documentation
```

## 🐛 Troubleshooting

### "Python not found" error
- **Windows**: Make sure Python was added to PATH during installation
- **Mac/Pi**: Use `python3` instead of `python`

### "Module not found" error
- Make sure virtual environment is activated (you should see `(venv)`)
- Reinstall requirements: `pip install -r requirements.txt`

### Ollama connection error
- Check if Ollama is running: `ollama list`
- If using network Ollama, check the IP address in config.py
- Try: `ollama serve` in a separate terminal

### Tkinter not found
- **Windows**: Reinstall Python with default options
- **macOS**: `brew install python-tk`
- **Raspberry Pi**: `sudo apt-get install python3-tk`

## 👥 For Instructors

- Pre-download Ollama models to save time
- Consider running Ollama on a single machine for all students
- Test network connectivity before class
- Have a fallback plan with pre-written story responses

## 📚 Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Ollama Documentation](https://github.com/ollama/ollama)

## 📄 License

This project is for educational purposes. [MIT License](./LICENSE).