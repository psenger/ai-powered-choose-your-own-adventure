"""
SUPER SIMPLE Choose Your Own Adventure Game
Everything in ONE FILE - Perfect for kids!
"""


def play_game():
    print("🎮 Welcome to the Adventure Game!")
    print("You are standing at the edge of a dark forest.")
    print("=" * 30)  # Print a decorative line

    print("\nWhat do you want to do?")
    print("1. Go into the forest")
    print("2. Walk around the forest")
    print("3. Go home")

    choice = input("Pick a number (1, 2, or 3): ")

    if choice == "1":
        print("You picked 1, and get lost. The end.")
    if choice == "2":
        print("You picked 2, and walk around the forest.")
    if choice == "3":
        print("You picked 3, and walk home because you can smell baking cookies.")


# Start the game
if __name__ == "__main__":
    play_game()