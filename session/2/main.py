# WHAT IS A FUNCTION? 🚀
#
# A function is like a little machine that does a job for you!
# Think of it like a sandwich maker - you put in bread and fillings,
# and it gives you back a yummy sandwich! 🥪 but you can keep doing
# it over and over again.

# Here's a super simple function that says hello:
def say_hello():
    # This is INSIDE the function - it's what the function DOES
    print("G'day mate! Welcome to our awesome game!")
    print("Hope you're ready for an adventure!")


# Here's a function that takes information (we call this a "parameter"):
def greet_player(player_name):
    # The "player_name" is like a box that holds whatever name we give it
    print(f"Hello {player_name}! Ready to play?")
    # The "f" before the quotes lets us put variables inside with {curly brackets}


# Here's a function that GIVES BACK an answer (we call this "returning"):
def add_numbers(first_number, second_number):
    # This function takes two numbers and adds them together
    result = first_number + second_number
    # "return" means "give back this answer to whoever asked"
    return result


# Here's a function that asks a question and gives back the answer:
def ask_favorite_color():
    # This function talks to the player and remembers their answer
    color = input("What's your favorite color? ")
    return color  # Give the color back to whoever called this function


# Now let's USE our functions! This is called "calling" a function:
print("# Let's test our functions!")
print()

# Call the hello function (no brackets needed for info):
say_hello()
print()

# Call the greet function and give it a name:
greet_player("Sarah")
greet_player("Jake")
print()

# Use the add function and save the answer:
my_answer = add_numbers(5, 3)
print(f"5 + 3 = {my_answer}")
print()

# Use the color function:
their_color = ask_favorite_color()
print(f"Cool! {their_color} is a bonzer color!")
print()

# 🤔 WHY USE FUNCTIONS?
# 1. You can use the same code over and over without typing it again
# 2. If you need to fix something, you only fix it in ONE place
# 3. It makes your code easier to read - like having chapters in a book
# 4. You can test each part separately to make sure it works
# 5. Other programmers can understand your code better

print("=" * 40)
print("NOW THE MYSTERIOUS __name__ THING!")
print("=" * 40)

# The __name__ thing is like Python's way of asking:
# "Am I the main program, or am I being used by another program?"

# When you run THIS file directly, __name__ equals "__main__"
# When another program imports this file, __name__ equals the filename

print(f"Right now, __name__ is: {__name__}")

# This is like a security guard for your code:
if __name__ == "__main__":
    # This code ONLY runs if someone runs THIS file directly
    # It WON'T run if another program just wants to borrow our functions
    print()
    print("🎮 You ran this file directly, so I'll run the main program!")
    print("This is like the 'main entrance' to our program")

    # Let's use all our functions together:
    print("\n--- MAIN PROGRAM STARTS HERE ---")
    say_hello()

    # Get the player's name and greet them
    player_name = input("What's your name? ")
    greet_player(player_name)

    # Do some math
    print(f"\nLet's do some math, {player_name}!")
    answer = add_numbers(10, 25)
    print(f"I calculated 10 + 25 = {answer}")

    # Ask about their favorite color
    color = ask_favorite_color()
    print(f"I'll remember that {player_name} likes {color}!")

    print("\n🏁 Program finished! That's how functions work!")

else:
    # This would run if another program imported our functions
    print("Someone else is using my functions - that's fine!")

# 🎓 WHAT DID WE LEARN?
# - Functions are like little machines that do jobs
# - You can give them information (parameters)
# - They can give back answers (return values)
# - The __name__ trick lets you have code that only runs when needed
# - Functions make your code cleaner, easier to fix, and reusable!
#
# Next time you see a function, think: "What job does this machine do?"
# And when you write code, think: "Could this be a useful machine for later?"