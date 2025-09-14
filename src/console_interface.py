"""
Console Interface - PRE-BUILT, MINIMAL MODIFICATIONS

INSTRUCTOR NOTES:
This file handles all the user interaction through the terminal/console.
Students should understand what this does but NOT modify it heavily.
The focus should be on game logic, not interface programming.

Key concepts to explain:
1. Classes and objects (ConsoleInterface is a class)
2. Methods (functions that belong to a class)
3. Input validation and error handling
4. Simple loops and user interaction
5. String formatting and output

Students can explore this file but should focus on game_manager.py and situations.py
"""

import game_manager
import config

class ConsoleInterface:
    """
    Handles all console-based user interaction
    
    INSTRUCTOR: This creates a simple text-based interface.
    Much simpler than GUI programming - just input() and print()!
    Students can see exactly how user input is processed.
    """
    
    def __init__(self):
        """
        Set up the console interface
        
        INSTRUCTOR: This runs when we create a ConsoleInterface()
        It creates the game manager that handles all the game logic.
        """
        self.game = game_manager.GameManager()
        
        # Debug info for instructors
        if config.DEBUG_MODE:
            print("🔧 DEBUG: Console interface created")
    
    def start_game(self):
        """
        Main game loop - keeps running until game ends
        
        INSTRUCTOR: This is the heart of the game interface.
        It shows the current situation, gets player input, and processes it.
        Students can see the clear input → process → output cycle.
        Also handles Ctrl+C gracefully for a better user experience.
        """
        
        try:
            # Game introduction
            self.show_welcome()
            
            # Start at the beginning
            self.display_situation("start")
            
            # Main game loop - keeps running until player quits or game ends
            while True:
                choice = self.get_player_choice()
                
                if choice == -1:  # Invalid input - try again
                    continue
                
                if choice == "quit":  # Player wants to quit
                    self.show_goodbye()
                    break
                    
                # Process the choice through game manager
                result = self.game.process_choice(choice)
                
                if isinstance(result, str):  # Error message from game
                    print(f"❌ {result}")
                    print("Try a different choice!")
                    continue
                
                # Check if game is over
                if self.game.is_game_over():
                    print("\n💀 GAME OVER!")
                    play_again = input("Would you like to play again? (y/n): ").lower()
                    if play_again.startswith('y'):
                        self.game = game_manager.GameManager()  # Reset game
                        self.display_situation("start")
                    else:
                        self.show_goodbye()
                        break
                else:
                    # Move to next situation
                    self.display_situation(self.game.current_situation)
                    
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            self.show_interrupt_goodbye()
    
    def show_welcome(self):
        """
        Display welcome message and instructions
        
        INSTRUCTOR: Students can modify this to personalize their game!
        """
        print("\n" + "=" * 60)
        print("🎮 WELCOME TO THE AI ADVENTURE GAME! 🎮")
        print("=" * 60)
        print(f"👋 Hello, {config.PLAYER_NAME}!")
        print("\n📖 How to play:")
        print("• Read each situation carefully")
        print("• Type the number of your choice and press Enter")
        print("• Type 'quit' anytime to exit the game")
        print("• Have fun and be creative!")
        print("=" * 60)
        
        if config.DEBUG_MODE:
            print("🔧 DEBUG MODE: Extra information will be shown")
            print("=" * 60)
    
    def display_situation(self, situation_id):
        """
        Show current situation and available choices
        
        INSTRUCTOR: This is where students see their situations.py changes!
        Point out how the situation data becomes formatted output.
        """
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Displaying situation '{situation_id}'")
        
        try:
            # Get situation data from game manager
            situation = self.game.get_situation(situation_id)
            
            # Clear visual separation
            print("\n" + "=" * 60)
            
            # Show title with emoji
            print(f"📖 {situation['title']}")
            print("=" * 60)
            
            # Show description (might be AI-enhanced in later sessions)
            print(situation['description'])
            
            # Show available choices
            print("\n" + "🎯 Your Choices:")
            for i, choice in enumerate(situation['choices'], 1):
                choice_text = choice['text']
                
                # Show requirements if any (Day 3+ feature)
                if choice.get('requires'):
                    required_items = ', '.join(choice['requires'])
                    choice_text += f" (Requires: {required_items})"
                
                print(f"  {i}. {choice_text}")
            
            # Show player status
            self.display_status()
            
            # Show situation ID if debug mode (helps instructors and students)
            if config.SHOW_SITUATION_IDS:
                print(f"\n🔧 Situation ID: {situation_id}")
                
        except KeyError as e:
            # Handle missing situations gracefully
            print(f"\n❌ ERROR: Situation '{situation_id}' not found!")
            print("This might be a typo in the 'next' field of a choice.")
            print("Check your situations.py file for spelling mistakes.")
            
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: {e}")
            
            # Fallback to start
            print("\nReturning to the beginning...")
            self.game.current_situation = "start"
            self.display_situation("start")
    
    def get_player_choice(self):
        """
        Get and validate player input
        
        INSTRUCTOR: Show students how input validation works.
        This prevents crashes from invalid input and gives helpful error messages.
        """
        
        try:
            # Get input from player
            user_input = input("\n👉 Enter your choice (number or 'quit'): ").strip().lower()
            
            # Check for quit command
            if user_input == 'quit' or user_input == 'q':
                return "quit"
            
            # Try to convert to number
            choice_num = int(user_input)
            
            # Check if choice number is valid
            current_situation = self.game.get_situation(self.game.current_situation)
            max_choices = len(current_situation['choices'])
            
            if 1 <= choice_num <= max_choices:
                if config.DEBUG_MODE:
                    print(f"🔧 DEBUG: Player chose option {choice_num}")
                return choice_num - 1  # Convert to 0-based index for programming
            else:
                print(f"❌ Invalid choice! Please enter a number between 1 and {max_choices}")
                return -1
                
        except ValueError:
            # Player didn't enter a number
            print("❌ Please enter a number (or 'quit' to exit)!")
            return -1
        except Exception as e:
            # Unexpected error
            print(f"❌ Something went wrong: {e}")
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Unexpected error in get_player_choice: {e}")
            return -1
    
    def display_status(self):
        """
        Show current player status (health, inventory, etc.)
        
        INSTRUCTOR: Students will see their config.py changes reflected here!
        This shows how different parts of the program work together.
        """
        
        # Get current game state
        health = self.game.health
        max_health = config.MAX_HEALTH
        
        # Format inventory nicely
        if self.game.inventory:
            items_text = ", ".join(self.game.inventory)
        else:
            items_text = "None"
        
        # Display status with emojis for engagement
        print(f"\n💪 Health: {health}/{max_health} | 🎒 Items: {items_text}")
        
        # Show story progress (optional)
        if config.DEBUG_MODE and self.game.story_history:
            print(f"🔧 DEBUG: Choices made: {len(self.game.story_history)}")
            print(f"🔧 DEBUG: Last 3 choices: {self.game.story_history[-3:]}")
    
    def show_goodbye(self):
        """
        Display goodbye message when player quits
        
        INSTRUCTOR: Students can customize this too!
        """
        print("\n" + "=" * 60)
        print("👋 Thanks for playing the AI Adventure Game!")
        print(f"🎯 You made {len(self.game.story_history)} choices in your adventure")
        print("📚 Keep learning Python and building amazing games!")
        print("=" * 60)
        print("🎮 Game created by: Year 3-5 Python students")
        print("=" * 60)
    
    def show_interrupt_goodbye(self):
        """
        Display goodbye message when player uses Ctrl+C
        
        INSTRUCTOR: This handles KeyboardInterrupt gracefully.
        Students will appreciate not seeing ugly Python tracebacks!
        """
        print("\n\n" + "=" * 60)
        print("⚡ Game interrupted! (Ctrl+C pressed)")
        print("👋 Thanks for playing the AI Adventure Game!")
        if hasattr(self.game, 'story_history') and self.game.story_history:
            print(f"🎯 You made {len(self.game.story_history)} choices before leaving")
        print("📚 Keep learning Python and building amazing games!")
        print("=" * 60)
        print("💡 Tip: Type 'quit' next time for a normal exit!")
        print("=" * 60)

"""
INSTRUCTOR TEACHING POINTS:

1. SIMPLE INPUT/OUTPUT:
   - Show how input() gets text from the player
   - Demonstrate how print() displays information
   - Much simpler than GUI programming!

2. INPUT VALIDATION:
   - Point out the try/except blocks
   - Show how we check if input is valid
   - Explain why this prevents crashes

3. LOOPS AND FLOW CONTROL:
   - The while True loop keeps the game running
   - Show how 'continue' and 'break' control the loop
   - Demonstrate the clear input → process → output cycle

4. STRING FORMATTING:
   - Point out f-strings like f"Health: {health}"
   - Show how emojis make output more engaging
   - Demonstrate text alignment and formatting

5. ERROR HANDLING:
   - Show graceful handling of missing situations
   - Demonstrate helpful error messages
   - Point out debug information for development

6. CLASS STRUCTURE:
   - ConsoleInterface handles user interaction
   - GameManager handles game logic
   - Clear separation of responsibilities

STUDENT ACTIVITIES FOR LATER SESSIONS:

Day 1:
- Run the game and see how their config changes appear
- Observe how situations.py content is displayed
- Try invalid inputs to see error handling

Day 2:
- Add their own situations and see them in the console
- Modify welcome/goodbye messages
- Add more status information

Day 3:
- See inventory system working in console
- Watch requirement checking in action
- Add custom status displays

Day 4-5:
- Observe AI enhancements in the console output
- Add custom formatting for AI responses
- Implement save/load features (advanced)

DEBUGGING TIPS:
- Use DEBUG_MODE in config.py to see extra information
- Add print() statements to see what's happening
- Check console output for error messages
- Test with invalid inputs to ensure robustness
"""