"""
Story Database - STUDENTS EXTEND THIS

INSTRUCTOR NOTES:
This file contains the heart of our adventure game - all the story situations!
This is where students will spend most of their creative time.

Key concepts to explain:
1. Dictionaries - like a real dictionary, each situation has a "key" and information
2. Nested data structures - dictionaries inside dictionaries
3. Lists of dictionaries - multiple choices in each situation
4. How the game flows from one situation to another

STUDENT ACTIVITIES:
- Read and understand the example situations
- Modify descriptions to make them more exciting
- Add new situations by copying the pattern
- Create branching storylines
"""

# The main story database - each situation is a dictionary
# INSTRUCTOR: Explain this is like a choose-your-own-adventure book in code form
SITUATIONS = {
    # Each key (like "start") is a situation ID
    # Each value is a dictionary with all the situation information
    
    "start": {
        # Basic information about this part of the story
        "title": "🌲 The Mysterious Forest",
        "description": """You stand at the edge of a dark, mysterious forest. 
Ancient trees tower above you, their branches creating shadows that dance in the wind. 
Two worn paths stretch ahead into the unknown. What do you choose?""",
        
        # List of choices the player can make
        # INSTRUCTOR: Show how each choice is its own dictionary
        "choices": [
            {
                "text": "🚶‍♀️ Take the left path through the thick trees",
                "next": "left_path",          # Which situation comes next
                "requires": []               # Items needed (empty = no requirements)
            },
            {
                "text": "🚶‍♂️ Take the right path along the stream", 
                "next": "right_path",
                "requires": []
            },
            {
                "text": "🏠 Go back home (you're too scared!)",
                "next": "end_coward",
                "requires": []
            }
        ],
        "image": "forest.txt"  # ASCII art file (optional)
    },
    
    "left_path": {
        "title": "🧚‍♀️ The Fairy Grove",
        "description": """You discover a magical grove filled with glowing mushrooms! 
Tiny lights dance between the trees, and you hear the gentle sound of wind chimes. 
This place feels alive with magic. The mushrooms pulse with a soft, blue light.""",
        
        "choices": [
            {
                "text": "🍄 Touch one of the glowing mushrooms",
                "next": "mushroom_magic",
                "requires": []
            },
            {
                "text": "👋 Call out 'Hello!' to the magical creatures",
                "next": "fairy_friend", 
                "requires": []
            },
            {
                "text": "🧺 Collect some mushrooms for later",
                "next": "mushroom_collect",
                "requires": ["basket"]  # Student activity: explain requirements
            }
        ],
        "image": "grove.txt"
    },
    
    "right_path": {
        "title": "🏰 The Old Stone Bridge", 
        "description": """You follow a babbling stream until you reach an ancient stone bridge. 
The bridge looks very old, with moss growing on its sides. 
Below, the water is crystal clear and you can see colorful fish swimming. 
On the other side, you spot what looks like a castle tower!""",
        
        "choices": [
            {
                "text": "🌉 Cross the bridge carefully",
                "next": "bridge_cross",
                "requires": []
            },
            {
                "text": "🎣 Try to catch a fish with your hands", 
                "next": "fishing_attempt",
                "requires": []
            },
            {
                "text": "🔍 Look under the bridge for treasures",
                "next": "bridge_treasure",
                "requires": []
            }
        ]
    },
    
    # Example of an ending situation
    "end_coward": {
        "title": "🏠 Safe at Home",
        "description": """You decide the forest is too scary and head back home. 
Your family welcomes you back, and you spend the evening reading adventure books by the fire. 
Maybe you'll be braver tomorrow... but for now, you're safe and sound!
        
🎮 GAME OVER - Try again and be more brave!""",
        
        "choices": [
            {
                "text": "🔄 Start a new adventure",
                "next": "start",
                "requires": []
            }
        ]
    },
    
    # Student will add more situations here!
    # INSTRUCTOR: Show students how to copy this pattern
    
    "mushroom_magic": {
        "title": "✨ Magical Transformation!",
        "description": """When you touch the mushroom, you feel a warm tingling sensation! 
Suddenly, you can understand the language of the forest animals. 
A friendly squirrel approaches and offers to be your guide.""",
        
        "choices": [
            {
                "text": "🐿️ Follow the squirrel guide",
                "next": "squirrel_guide",
                "requires": []
            },
            {
                "text": "🦋 Try talking to a beautiful butterfly",
                "next": "butterfly_chat", 
                "requires": []
            }
        ]
    },
    
    "fairy_friend": {
        "title": "🧚‍♀️ A Tiny New Friend",
        "description": """A tiny fairy appears, no bigger than your thumb! 
She has gossamer wings and wears a dress made of flower petals. 
'Hello, young adventurer!' she says in a voice like tinkling bells. 
'I can grant you one small gift to help on your journey!'""",
        
        "choices": [
            {
                "text": "🗺️ Ask for a magical map",
                "next": "get_magic_map",
                "requires": []
            },
            {
                "text": "🏃‍♂️ Ask for super speed",
                "next": "get_super_speed",
                "requires": []
            },
            {
                "text": "💎 Ask for a lucky charm",
                "next": "get_lucky_charm", 
                "requires": []
            }
        ]
    }
    
    # INSTRUCTOR NOTE: More situations will be added in later sessions
    # Students should add their own situations following this pattern
}

# Inventory items and their effects (Day 3 focus)
# INSTRUCTOR: This will become important when we add the inventory system
ITEMS = {
    "basket": {
        "name": "🧺 Woven Basket", 
        "description": "A sturdy basket perfect for carrying forest treasures"
    },
    "torch": {
        "name": "🔦 Bright Torch", 
        "description": "A magical torch that never burns out"
    },
    "key": {
        "name": "🗝️ Golden Key", 
        "description": "An ornate key that opens mysterious locks"
    },
    "map": {
        "name": "🗺️ Magic Map",
        "description": "A map that shows secret paths through the forest"
    },
    "charm": {
        "name": "💎 Lucky Charm",
        "description": "A sparkling gem that brings good fortune"
    }
}

"""
INSTRUCTOR TEACHING POINTS:

1. DICTIONARY STRUCTURE:
   - Show how each situation is like a filing cabinet
   - The key (like "start") is the label on the drawer
   - The value (the dictionary) is everything inside the drawer
   - Demonstrate: SITUATIONS["start"] gets the start situation

2. NESTED DICTIONARIES:
   - Point out how choices are dictionaries inside the main dictionary
   - Show the pattern: text, next, requires
   - Explain how "next" connects situations together

3. LISTS AND DICTIONARIES TOGETHER:
   - The "choices" key contains a LIST of dictionaries
   - Each choice is its own dictionary with the same structure
   - Show how to access: SITUATIONS["start"]["choices"][0]["text"]

4. STUDENT ACTIVITIES:
   - Have students modify descriptions to be more exciting
   - Show them how to add a new situation by copying the pattern
   - Demonstrate how "next" values must match situation keys
   - Practice adding choices that connect to existing situations

5. CREATIVE WRITING CONNECTION:
   - Connect this to English class - story structure, plot development
   - Encourage creative descriptions with sensory details
   - Show how choices create branching narratives

COMMON MISTAKES TO WATCH FOR:
- Missing commas between dictionary items
- Typos in "next" values that don't match situation keys  
- Forgetting quotes around strings
- Missing square brackets around choice lists
- Incorrect indentation (Python is picky about this!)

DEBUGGING TIPS FOR STUDENTS:
- If you get an error, check for missing commas
- Make sure "next" situation names exist in SITUATIONS
- Count your opening and closing brackets/braces
- Ask a friend to proofread your punctuation
"""