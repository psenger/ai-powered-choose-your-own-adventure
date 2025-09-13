# Daily Objectives

## Day 1: Introduction & Setup (1.5 hours)

### Environment Setup (30 minutes)
- Get everyone's Python environment working
- Ensure Python 3.11+ is installed (no additional libraries needed!)
- install VS Code + Extensions
- Clone the git repository successfully
- Create virtual environment: `python3 -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
- Install required packages: `pip install -r requirements.txt`
- Test the game runs: `python3 hello-world.py`
- Test VS Code with Python extension - hello-world.py

#### Required Libraries
- **No external dependencies for Day 1-3!** (Pure Python standard library)
- **requests**: For AI features in Days 4-5 (`pip install requests`)
- **Optional**: pytest, black for development tools

#### Setup Commands

```bash
# Clone the repository
git clone git@github.com:psenger/ai-powered-choose-your-own-adventure.git ai-powered-choose-your-own-adventure
chmod +x load_session.sh

# start session 1
./load_session.sh

# Create and activate virtual environment (IMPORTANT!)
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# OR install everything from requirements file
pip install -r requirements.txt

# Test if everything works - simple console interface!
python3 src/hello-world.py

# When done, deactivate virtual environment
deactivate
```

### Code Exploration (30 minutes)
- Run the base game and understand the console interface
- Explore the code structure and file organization
- Understand the role of each file (main.py, config.py, situations.py, console_interface.py)
- Navigate through the game flow using keyboard input

### Simple Modifications (30 minutes)
- Modify simple values in config.py (health, player name)
- Edit one situation description in situations.py
- Run and test changes to see immediate results

### Key Learning Concepts
- **Variables and data types**: Understanding strings, integers, and basic Python syntax
- **Data structures**: Introduction to dictionaries and how they store game situations
- **Running Python programs**: Using the command line or IDE to execute code
- **Basic debugging**: Using print statements to understand program flow

### Student Tasks Checklist
- [ ] Successfully install Python 3.11+ and verify with `python3 --version`
- [ ] Create virtual environment with `python3 -m venv .venv`
- [ ] Activate virtual environment (`source .venv/bin/activate` or `.venv\Scripts\activate`)
- [ ] Install required packages with `pip install -r requirements.txt`
- [ ] Successfully run the console adventure game with `python3 src/hello-world.py`
- [ ] Navigate through the game using number choices and Enter key
- [ ] Change player starting health in config.py (try 50, 150, 200)
- [ ] Modify their character name in config.py to their own name
- [ ] Edit one situation description in situations.py to make it more exciting
- [ ] Run and test all changes work correctly in the terminal
- [ ] Understand what each main file does (main.py, config.py, situations.py, console_interface.py)
- [ ] Learn to deactivate virtual environment with `deactivate`

### Success Criteria
By the end of Day 1, students should:
- Have a working development environment
- Understand basic Python variables and data structures (especially dictionaries)
- Have successfully modified and tested simple game elements
- Feel confident running and testing Python code

