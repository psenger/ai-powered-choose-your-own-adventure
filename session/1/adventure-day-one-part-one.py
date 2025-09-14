# SUPER SIMPLE Choose Your Own Adventure Game
# Everything in ONE FILE
#
# 🚨 WARNING: This code is a bit dodgy! 🚨
# It works, but it's got some fair dinkum problems that we'll fix later!
# This is what we call "spaghetti code" - messy like dropped snags at a barbie!


def play_game():
    # This function runs our whole game - pretty simple, eh?
    #
    # 🤔 WHAT'S DODGY HERE:
    # - This function does EVERYTHING! That's like trying to play cricket, 
    #   footy, and netball all at the same time - bit mental!
    # - No error checking - what if someone types "banana" instead of 1, 2, or 3?
    # - The story just STOPS after one choice - that's not much of an adventure!
    # - Same boring responses every time - no randomness, no excitement!
    
    # Print the welcome message - this bit's actually pretty good!
    print("🎮 Welcome to the Adventure Game!")
    
    # Set up the scene - this is called "exposition" in fancy writing terms
    print("You are standing at the edge of a dark forest.")
    
    # Make a decorative line using string multiplication (pretty clever trick!)
    # The "=" character gets repeated 30 times
    print("=" * 30)  # Print a decorative line

    # Show the player their choices - this is the "decision point"
    print("\nWhat do you want to do?")  # \n makes a new line (blank line above this)
    print("1. Go into the forest")      # Choice option 1
    print("2. Walk around the forest")  # Choice option 2  
    print("3. Go home")                 # Choice option 3

    # Get input from the player
    # 🚨 PROBLEM ALERT! 🚨 
    # What if they type "ONE" or "first" or "asdfgh"? This code will break like a busted thong!
    choice = input("Pick a number (1, 2, or 3): ")

    # Handle the different choices using if statements
    # 🚨 ANOTHER PROBLEM! 🚨
    # These should be "elif" statements, not separate "if" statements!
    # Right now, if someone hacks the code, ALL the if statements could run!
    # Also, what happens if they don't pick 1, 2, or 3? NOTHING! The game just ends!
    # That's like asking "Do you want ice cream?" and when they say "Maybe", you just walk away!
    
    if choice == "1":
        # Forest choice - bit of a bummer ending, this one!
        print("You picked 1, and get lost. The end.")
        # 🤔 This ending is pretty rubbish - no adventure, just "you lose"!
        
    if choice == "2":  # 🚨 Should be "elif choice == '2':" 
        # Walk around choice - doesn't really lead anywhere
        print("You picked 2, and walk around the forest.")
        # 🤔 Then what happens? Do you find something? See a koala? Code just stops!
        
    if choice == "3":  # 🚨 Should be "elif choice == '3':"
        # Go home choice - actually not too bad, gives a reason (cookies!)
        print("You picked 3, and walk home because you can smell baking cookies.")
        # 🤔 This is actually the most complete response, but still pretty short!

    # 🚨 MEGA PROBLEM! 🚨
    # What if someone types "4" or "banana" or "I don't know"?
    # The program just ends with no message - that's like a shopkeeper 
    # ignoring you when you ask for help! Super rude!
    
    # 🤔 OTHER ISSUES WITH THIS CODE:
    # 1. No way to play again - one shot and you're done!
    # 2. No character names or personality
    # 3. No inventory system (what if you find a torch or something?)
    # 4. No score keeping
    # 5. No save/load game feature
    # 6. Stories are really short - like a book with only one sentence per page!
    # 7. No graphics or sound effects (fair enough for console, but still!)
    # 8. No difficulty levels
    # 9. Same story every time - gets boring quick!
    # 10. Code all squished into one function - that's like putting your 
    #     entire bedroom, kitchen, and bathroom into one tiny room!


# This is the "main" part - it only runs when you run THIS file directly
# Not when you import it into another program (pretty smart Python trick!)
if __name__ == "__main__":
    # Start the game by calling our play_game function
    play_game()
    
    # 🤔 WHAT SHOULD HAPPEN HERE:
    # - Maybe ask if they want to play again?
    # - Show some game statistics?
    # - Thank them for playing?
    # - Right now it just... ends. Like a TV show that cuts off mid-sentence!

#
# 🎓 WHAT WE'LL LEARN TO FIX:
#
# SESSION 2: We'll add a proper GUI (Graphical User Interface) with buttons and windows!
#            No more typing numbers - just click what you want! Bonzer!
#
# SESSION 3: We'll make the choices actually DO something interesting!
#            Multiple story paths, character development, inventory items!
#
# SESSION 4: We'll add AI to make the stories more interesting and random!
#            The computer will help write new adventures every time!
#
# SESSION 5: We'll put it all together into a proper game with save files,
#            settings, and maybe even sound effects! Fair dinkum adventure!
#
# This code is like a rough sketch before painting a masterpiece - 
# it shows the basic idea, but there's heaps of room for improvement!
# That's totally fine - every programmer starts with simple code like this!
#
# Remember: The best way to learn is to start with something that works 
# (even if it's a bit ordinary) and then make it better bit by bit!
# That's how you become a ripper programmer! 🇦🇺