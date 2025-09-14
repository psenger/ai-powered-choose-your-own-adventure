"""
Game Logic Manager - STUDENTS HEAVILY MODIFY THIS

INSTRUCTOR NOTES:
This is the heart of the game logic where students will make most of their changes.
This file connects the GUI to the story data and manages the game state.

Key concepts to explain:
1. Classes and objects (GameManager is a class)
2. Instance variables (self.health, self.inventory, etc.)
3. Methods (functions that belong to a class)
4. How different files work together

STUDENT FOCUS AREAS:
- Understanding how game state is tracked
- Modifying the choice processing logic
- Adding new game features (inventory, health changes)
- Connecting to the AI system (later sessions)
"""

import situations
import config
from typing import List, Dict

# Import AI module for later sessions (will be simple stub for Day 1)
try:
    import ai_storyteller
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    if config.DEBUG_MODE:
        print("🔧 DEBUG: AI module not available yet (normal for Day 1)")

class GameManager:
    """
    Manages the game state and logic
    
    INSTRUCTOR: This class keeps track of everything that happens in the game.
    Think of it like the game's "brain" - it remembers where you are,
    what you have, and how much health you have.
    """
    
    def __init__(self):
        """
        Initialize a new game
        
        INSTRUCTOR: This runs when we start a new game.
        All the starting values come from config.py (students can modify those!)
        """
        
        # Game state variables - INSTRUCTOR: Show how these track the game
        self.current_situation = "start"                    # Where we are in the story
        self.inventory = list(config.STARTING_INVENTORY)    # What items we have
        self.health = config.STARTING_HEALTH                # How much health we have
        self.story_history = []                             # What choices we've made
        
        # AI storyteller (will be used in later sessions)
        if AI_AVAILABLE and config.AI_ENABLED:
            self.ai = ai_storyteller.AIStoryteller()
        else:
            self.ai = None
        
        # Debug info for instructors
        if config.DEBUG_MODE:
            print("🔧 DEBUG: New game started")
            print(f"🔧 DEBUG: Starting health: {self.health}")
            print(f"🔧 DEBUG: Starting inventory: {self.inventory}")
            print(f"🔧 DEBUG: AI enabled: {config.AI_ENABLED and AI_AVAILABLE}")
    
    def get_situation(self, situation_id: str) -> Dict:
        """
        Get information about a story situation
        
        INSTRUCTOR: This gets the situation data from situations.py
        Students will see their situation modifications appear here.
        
        Args:
            situation_id: The ID of the situation (like "start" or "left_path")
            
        Returns:
            Dictionary with situation information (title, description, choices)
        """
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Getting situation '{situation_id}'")
        
        try:
            # Get the basic situation from situations.py
            # INSTRUCTOR: Show students how this connects to their situations file
            base_situation = situations.SITUATIONS[situation_id].copy()
            
            # AI enhancement (Day 4-5 feature - just a placeholder for now)
            if self.ai and config.AI_ENABLED:
                # This will be implemented in later sessions
                enhanced_desc = self.ai.enhance_description(
                    base_situation["description"],
                    self.story_history
                )
                base_situation["description"] = enhanced_desc
                
                if config.DEBUG_MODE:
                    print("🔧 DEBUG: Description enhanced by AI")
            
            return base_situation
            
        except KeyError:
            # Handle missing situations gracefully
            error_situation = {
                "title": "❌ Error",
                "description": f"Oops! The situation '{situation_id}' doesn't exist. This might be a typo in the story connections.",
                "choices": [
                    {
                        "text": "🔄 Go back to the start",
                        "next": "start",
                        "requires": []
                    }
                ]
            }
            
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG ERROR: Situation '{situation_id}' not found!")
            
            return error_situation
    
    def process_choice(self, choice_index: int):
        """
        Handle when a player makes a choice
        
        INSTRUCTOR: This is called every time a student selects an option.
        This is where students will add new game features like inventory changes,
        health effects, and special game logic.
        
        Args:
            choice_index: Which choice the player selected (0, 1, 2, etc.)
            
        Returns:
            None if successful, or error message string if choice can't be made
        """
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Processing choice {choice_index}")
        
        try:
            # Get current situation and the chosen option
            current = situations.SITUATIONS[self.current_situation]
            choice = current["choices"][choice_index]
            
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Choice text: '{choice['text']}'")
                print(f"🔧 DEBUG: Next situation: '{choice['next']}'")
            
            # Check if player has required items (Day 3+ feature)
            # INSTRUCTOR: This will become important when we add inventory system
            if not self.check_requirements(choice.get("requires", [])):
                required_items = ", ".join(choice["requires"])
                error_msg = f"You need these items to do that: {required_items}"
                
                if config.DEBUG_MODE:
                    print(f"🔧 DEBUG: Choice blocked - missing items: {required_items}")
                
                return error_msg
            
            # Record this choice in our history
            self.story_history.append(choice["text"])
            
            # Move to the next situation
            self.current_situation = choice["next"]
            
            # Apply any effects from this choice (students will add this later)
            self.apply_choice_effects(choice)
            
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Moved to situation '{self.current_situation}'")
                print(f"🔧 DEBUG: Current health: {self.health}")
                print(f"🔧 DEBUG: Current inventory: {self.inventory}")
            
            return None  # Success
            
        except (KeyError, IndexError) as e:
            error_msg = f"Error processing choice: {e}"
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG ERROR: {error_msg}")
            return error_msg
    
    def check_requirements(self, required_items: List[str]) -> bool:
        """
        Check if player has all required items for a choice
        
        INSTRUCTOR: This will be important for Day 3 when we add inventory.
        For now, it just returns True since we don't have items yet.
        
        Args:
            required_items: List of item names needed for this choice
            
        Returns:
            True if player has all items, False otherwise
        """
        
        if not required_items:  # No requirements
            return True
        
        # Check if player has all required items
        # INSTRUCTOR: Students will understand this better on Day 3
        has_all_items = all(item in self.inventory for item in required_items)
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Checking requirements: {required_items}")
            print(f"🔧 DEBUG: Player inventory: {self.inventory}")
            print(f"🔧 DEBUG: Has all items: {has_all_items}")
        
        return has_all_items
    
    def apply_choice_effects(self, choice: Dict):
        """
        Apply any effects from making a choice (health changes, items, etc.)
        
        INSTRUCTOR: This is where students will add cool game features!
        For Day 1, this is mostly empty, but students will expand it later.
        
        STUDENT EXTENSION IDEAS:
        - Health changes based on choices
        - Finding or losing items
        - Special status effects
        - Score tracking
        
        Args:
            choice: The choice dictionary that was selected
        """
        
        # For Day 1, we don't have many effects yet
        # Students will add more here in later sessions!
        
        # Example effects that students might add later:
        # if "damage" in choice:
        #     self.health -= choice["damage"]
        #     if self.health < 0:
        #         self.health = 0
        
        # if "heal" in choice:
        #     self.health += choice["heal"]
        #     if self.health > config.MAX_HEALTH:
        #         self.health = config.MAX_HEALTH
        
        # if "find_item" in choice:
        #     self.inventory.append(choice["find_item"])
        
        if config.DEBUG_MODE:
            print("🔧 DEBUG: Applied choice effects (none for Day 1)")
    
    def add_item(self, item_name: str):
        """
        Add an item to the player's inventory
        
        INSTRUCTOR: This will be used in Day 3+ when we implement inventory.
        Students will use this to give players items they find.
        
        Args:
            item_name: Name of the item to add
        """
        
        if len(self.inventory) >= config.INVENTORY_LIMIT:
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Inventory full! Cannot add {item_name}")
            return False
        
        self.inventory.append(item_name)
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Added {item_name} to inventory")
            print(f"🔧 DEBUG: Current inventory: {self.inventory}")
        
        return True
    
    def remove_item(self, item_name: str):
        """
        Remove an item from the player's inventory
        
        INSTRUCTOR: Students might use this for items that get consumed.
        
        Args:
            item_name: Name of the item to remove
            
        Returns:
            True if item was removed, False if player didn't have it
        """
        
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Removed {item_name} from inventory")
                print(f"🔧 DEBUG: Current inventory: {self.inventory}")
            
            return True
        else:
            if config.DEBUG_MODE:
                print(f"🔧 DEBUG: Cannot remove {item_name} - not in inventory")
            
            return False
    
    def change_health(self, amount: int):
        """
        Change the player's health by a certain amount
        
        INSTRUCTOR: Students will use this for damage and healing effects.
        
        Args:
            amount: Positive numbers heal, negative numbers hurt
        """
        
        old_health = self.health
        self.health += amount
        
        # Keep health within bounds
        if self.health < config.MIN_HEALTH:
            self.health = config.MIN_HEALTH
        elif self.health > config.MAX_HEALTH:
            self.health = config.MAX_HEALTH
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Health changed from {old_health} to {self.health} (change: {amount})")
    
    def is_game_over(self) -> bool:
        """
        Check if the game should end
        
        INSTRUCTOR: Students might expand this with different end conditions.
        
        Returns:
            True if game should end, False if it continues
        """
        
        # Game ends if health reaches minimum
        if self.health <= config.MIN_HEALTH:
            if config.DEBUG_MODE:
                print("🔧 DEBUG: Game over - health too low")
            return True
        
        # Students might add other end conditions here
        # Example: if self.current_situation.startswith("end_"):
        #     return True
        
        return False
    
    def get_game_stats(self) -> Dict:
        """
        Get current game statistics
        
        INSTRUCTOR: This can be used for displaying game info or debugging.
        Students might expand this with more statistics.
        
        Returns:
            Dictionary with current game state information
        """
        
        stats = {
            "current_situation": self.current_situation,
            "health": self.health,
            "inventory": self.inventory.copy(),
            "story_history": self.story_history.copy(),
            "choices_made": len(self.story_history),
            "ai_enabled": self.ai is not None
        }
        
        if config.DEBUG_MODE:
            print(f"🔧 DEBUG: Current game stats: {stats}")
        
        return stats

"""
INSTRUCTOR TEACHING POINTS:

1. CLASS STRUCTURE:
   - GameManager is like the game's "brain"
   - __init__ sets up the starting state
   - Each method handles a specific aspect of the game

2. INSTANCE VARIABLES (self.something):
   - self.health tracks player health
   - self.inventory tracks what items they have
   - self.current_situation tracks where they are in the story
   - Show how these persist throughout the game

3. CONNECTING FILES:
   - Uses situations.SITUATIONS to get story data
   - Uses config values for starting health, inventory, etc.
   - Will connect to ai_storyteller in later sessions

4. ERROR HANDLING:
   - Show how try/except blocks handle missing situations
   - Demonstrate graceful error messages
   - Explain how this prevents crashes

5. DEBUGGING:
   - Point out all the DEBUG_MODE print statements
   - Show students how to use these to understand game flow
   - Encourage students to add their own debug prints

STUDENT ACTIVITIES FOR LATER SESSIONS:

Day 2:
- Modify apply_choice_effects to add simple health changes
- Add print statements to see game state changes

Day 3:
- Implement item finding in apply_choice_effects
- Add new methods for special game mechanics
- Connect inventory system to choice requirements

Day 4-5:
- Connect AI storyteller functionality
- Add more sophisticated game mechanics
- Implement save/load features (advanced students)

COMMON ISSUES TO WATCH FOR:
- Students forgetting to update situations.py when adding new "next" values
- Trying to access dictionary keys that don't exist
- Not understanding the difference between class variables and instance variables
- Confusion about when methods are called and in what order
"""