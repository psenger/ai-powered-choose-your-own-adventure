"""
Try-Catch (Exception Handling) Demo for Kids
=============================================
Learn how to handle errors gracefully in Python!
"""

print("=== Example 1: Dividing Numbers ===")
# Sometimes things go wrong - like dividing by zero!
try:
    number = 10
    divisor = 0
    result = number / divisor
    print(f"The answer is: {result}")
except ZeroDivisionError:
    print("Oops! You can't divide by zero, mate!")
    print("Let's try something else instead.")

print()

print("=== Example 2: Converting to a Number ===")
# What if someone types letters instead of numbers?
try:
    age = int("ten")  # This will cause an error!
    print(f"Your age is: {age}")
except ValueError:
    print("Crikey! That's not a number!")
    print("Please use digits like 10, not words like 'ten'")

print()

print("=== Example 3: Getting User Input Safely ===")
# Let's make a safe age checker
print("How old are you?")
try:
    user_age = int(input("Enter your age: "))
    print(f"You are {user_age} years old!")

    if user_age >= 8 and user_age <= 11:
        print("You're the perfect age for this program!")
    elif user_age < 8:
        print("You're pretty young! Keep learning!")
    else:
        print("You're getting older and wiser!")

except ValueError:
    print("That doesn't look like a number to me!")
    print("Next time, try typing just numbers like 9 or 10")

print()

print("=== Example 4: Multiple Errors ===")
# We can catch different types of errors
numbers = [5, 10, 15]

try:
    print("Trying to access index 10...")
    print(numbers[10])  # This list only has 3 items!
except IndexError:
    print("Fair dinkum! That index doesn't exist!")
    print(f"This list only has {len(numbers)} items")
except Exception as e:
    print(f"Some other error happened: {e}")

print()

print("=== Example 5: Try-Except-Finally ===")
# 'finally' always runs, no matter what!
try:
    print("Opening our lunchbox...")
    favourite_food = "vegemite sandwich"
    print(f"Found: {favorite_food}")  # Spelling error! Won't find the variable
except NameError:
    print("Couldn't find that food in the lunchbox!")
finally:
    print("Closing the lunchbox (this always happens!)")

print()
print("🎉 Great job learning about try-catch!")
print("Remember: try-catch helps your program keep running even when errors happen!")