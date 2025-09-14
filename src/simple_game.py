"""
SUPER SIMPLE Choose Your Own Adventure Game
Everything in ONE FILE - Perfect for kids!
"""

def play_game():
    print("🎮 Welcome to the Adventure Game!")
    print("You are standing at the edge of a dark forest.")
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Go into the forest")
        print("2. Walk around the forest")
        print("3. Go home")
        
        choice = input("Pick a number (1, 2, or 3): ")
        
        if choice == "1":
            forest_adventure()
        elif choice == "2":
            around_forest()
        elif choice == "3":
            go_home()
            break
        else:
            print("Please pick 1, 2, or 3!")

def forest_adventure():
    print("\n🌲 You walk into the dark forest...")
    print("You see a glowing mushroom!")
    
    print("\nWhat do you do?")
    print("1. Touch the mushroom")
    print("2. Walk past it")
    
    choice = input("Pick 1 or 2: ")
    
    if choice == "1":
        print("✨ The mushroom glows brighter! You feel magical!")
        print("You win! 🏆")
    elif choice == "2":
        print("You walk safely past and find treasure! 💰")
        print("You win! 🏆")
    else:
        print("The mushroom disappears. Try again!")

def around_forest():
    print("\n🚶 You walk around the forest...")
    print("You find a friendly dog! 🐕")
    print("The dog leads you to a hidden treasure! 💎")
    print("You win! 🏆")

def go_home():
    print("\n🏠 You go home safely.")
    print("Maybe you'll be braver next time!")
    print("Thanks for playing! 👋")

# Start the game
if __name__ == "__main__":
    play_game()