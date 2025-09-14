"""
Game Configuration File - STUDENTS MODIFY THIS

INSTRUCTOR NOTES:
This file contains all the settings that students can easily change.
This is perfect for Day 1 activities where students make simple modifications.

Key concepts to explain:
1. Variables and assignment (=)
2. Different data types (strings, numbers, booleans, lists)
3. How changing these values affects the game
4. Comments using # symbol

STUDENT ACTIVITIES:
- Change PLAYER_NAME to their own name
- Modify STARTING_HEALTH (try 50, 150, 200)
- Add items to STARTING_INVENTORY
- Experiment with different values and see what happens!
"""

# AI Settings (Day 4-5 - Advanced students only)
# INSTRUCTOR: Explain these are for later sessions
OLLAMA_URL = "http://localhost:11434"  # Where the AI lives
MODEL_NAME = "llama3.2"                # Which AI model to use
AI_ENABLED = False                     # Turn AI on/off (False for Day 1)

# Game Settings - STUDENTS CHANGE THESE!
# INSTRUCTOR: These are perfect for student experimentation
PLAYER_NAME = "Brave Adventurer"       # Student activity: Change to your name!
STARTING_HEALTH = 100                  # Student activity: Try different numbers
STARTING_INVENTORY = []                # Student activity: Add items like ["map", "snack"]

# Console Display Settings - STUDENTS CAN EXPERIMENT
# INSTRUCTOR: These control how the console output looks
CONSOLE_WIDTH = 60                     # Width of separator lines (=====)
USE_EMOJIS = True                      # Show emojis in output (🎮, 📖, etc.)

# Game Rules - STUDENTS CAN MODIFY LATER
# INSTRUCTOR: Explain these control game difficulty
MAX_HEALTH = 200                       # Highest health possible
MIN_HEALTH = 0                         # When you lose the game
INVENTORY_LIMIT = 10                   # How many items you can carry

# Debug Settings - FOR INSTRUCTORS
# INSTRUCTOR: Use these to help with teaching and debugging
DEBUG_MODE = False                     # Show extra information
SHOW_SITUATION_IDS = True              # Display situation names for debugging

"""
INSTRUCTOR TEACHING POINTS:

1. VARIABLES: 
   - Explain that variables are like labeled boxes that store information
   - Show how PLAYER_NAME = "Bob" stores the text "Bob" in a box called PLAYER_NAME
   - Demonstrate changing values and running the game to see effects

2. DATA TYPES:
   - Strings (text): "Brave Adventurer" - always in quotes
   - Numbers: 100, 50, 200 - no quotes needed
   - Booleans: True/False - special Python words
   - Lists: [] - can hold multiple items

3. DEBUGGING:
   - Show students how to print() variables to see their values
   - Example: print("Player name is:", PLAYER_NAME)
   - Use DEBUG_MODE to show extra information in the game

4. EXPERIMENTATION:
   - Encourage students to try extreme values (health = 1000000)
   - Show how changing FONT_SIZE affects readability
   - Demonstrate the inventory system with starting items

COMMON STUDENT MISTAKES TO WATCH FOR:
- Forgetting quotes around text: PLAYER_NAME = Bob (wrong) vs "Bob" (right)
- Using numbers in quotes: STARTING_HEALTH = "100" (wrong) vs 100 (right)
- Spelling mistakes in variable names
- Forgetting to save the file before testing
"""