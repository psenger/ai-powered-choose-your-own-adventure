"""
AI-Powered Choose Your Own Adventure Game
Entry Point - DO NOT MODIFY

INSTRUCTOR NOTES:
This is the starting point of our adventure game. When students run this file,
it starts the console-based adventure game.

Key concepts to explain:
1. Importing modules (bringing in code from other files)
2. The main() function as an entry point
3. How Python programs start execution
4. Simple console input/output

Students should understand this file but NOT modify it.
The focus should be on other files where they'll make changes.
"""

from src.console_interface import ConsoleInterface

def main():
    """
    Main function that starts the adventure game
    
    INSTRUCTOR EXPLANATION:
    - Creates a console interface object
    - Starts the game loop which handles all user interaction
    - Much simpler than GUI - just input() and print()!
    """
    print("🎮 Starting Adventure Game...")
    print("📚 Day 1 Learning: Understanding how programs start")
    print("💻 Console-based interface - no complex setup needed!")
    
    # Create the console interface
    game = ConsoleInterface()
    
    # Start the game loop
    game.start_game()

# This special line means "run main() when this file is executed directly"
# INSTRUCTOR NOTE: Explain this is Python's way of saying "start here"
if __name__ == "__main__":
    main()