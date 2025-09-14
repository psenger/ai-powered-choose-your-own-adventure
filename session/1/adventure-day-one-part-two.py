"""
SUPER SIMPLE Choose Your Own Adventure Game
Now with FUNCTIONS! Like a meat pie - everything has its own section!
Perfect for Aussie kids learning to code! 🇦🇺
"""


def show_welcome():
    """
    This function shows the welcome message
    Think of it like the front door of your house - everyone comes through here first!
    """
    print("🎮 G'day mate! Welcome to the Adventure Game!")
    print("You're standing at the edge of a dark forest.")
    print("It's darker than a wombat's burrow in there!")
    print("=" * 40)  # This makes a fancy line - like drawing with equals signs!


def show_choices():
    """
    This function shows all the choices to the player
    It's like a menu at Maccas - here are your options!
    """
    print("\nWhat do you reckon you should do?")
    print("1. Go into the forest (brave as a drop bear!)")
    print("2. Walk around the forest (smart as a kookaburra!)")
    print("3. Go home (sensible as a wombat!)")


def get_player_choice():
    """
    This function gets the player's choice and gives it back
    It's like asking "What flavour ice cream do you want?" and waiting for an answer

    PROGRAMMING GAP ALERT! 🚨
    This function doesn't check if the player types something silly like "banana" or "42"
    What happens if someone types "pizza"? The program might get as confused as a kangaroo in a shopping centre!
    """
    choice = input("Pick a number (1, 2, or 3): ")
    return choice  # This sends the choice back to whoever asked for it!


def handle_forest_choice():
    """
    This function handles what happens when you go into the forest
    Spoiler alert: it's not good! Like forgetting your hat on a 40-degree day!
    """
    print("You picked 1, and wandered into the forest!")
    print("You got lost faster than a tourist in the Outback!")
    print("The End. Better luck next time, mate! 🦘")


def handle_around_choice():
    """
    This function handles walking around the forest
    Much safer than going in - like staying in the shade on a hot day!
    """
    print("You picked 2, and walked around the forest!")
    print("Smart choice! You avoided getting lost and found some pretty flowers.")
    print("You're as wise as an old cockatoo! 🌸")


def handle_home_choice():
    """
    This function handles going home
    Sometimes the best adventure is a warm kitchen!
    """
    print("You picked 3, and headed straight home!")
    print("Good choice - you can smell your mum's lamingtons baking!")
    print("Adventures are great, but nothing beats home cooking! 🍰")


def handle_unknown_choice(choice):
    """
    This function handles when someone types something unexpected
    Like when your mate says they don't like Vegemite - totally unexpected!

    PROGRAMMING GAP FIXED! 🎉
    The original program didn't have this function - if you typed "koala"
    it would just ignore you like a grumpy echidna!
    """
    print(f"Crikey! You typed '{choice}' but that's not 1, 2, or 3!")
    print("That's more confusing than a platypus to a tourist!")
    print("Let's pretend you went home for some tucker instead! 🍽️")


def play_game():
    """
    This is the MAIN function - the boss of all the other functions!
    It tells all the other functions what to do and when to do it
    Like the conductor of an orchestra, but with more Python and less violins!

    PROGRAMMING GAP ALERT! 🚨
    This game only lets you make ONE choice and then it ends!
    Real adventures have lots of choices - like choosing between
    Tim Tams or Anzac biscuits (why not both?!)
    A better game would let you keep making choices until you decide to quit!
    """
    show_welcome()           # Show the welcome message
    show_choices()           # Show what the player can do
    choice = get_player_choice()  # Ask the player what they want to do

    # Now we decide what happens based on their choice
    # This is like a big sorting machine - each choice goes to its own place!
    if choice == "1":
        handle_forest_choice()      # Off to the forest!
    elif choice == "2":
        handle_around_choice()      # Around we go!
    elif choice == "3":
        handle_home_choice()        # Home sweet home!
    else:
        handle_unknown_choice(choice)  # Oops, something weird happened!


# This is where the magic starts!
# It's like saying "Python, please run my game now!"
if __name__ == "__main__":
    play_game()
    print("\nThanks for playing! See ya later, alligator! 🐊")