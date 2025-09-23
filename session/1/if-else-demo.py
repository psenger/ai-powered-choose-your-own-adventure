# 🤔 IF-THEN-ELSE - MAKING DECISIONS! 🤔
#
# Computers need to make decisions, just like people!
# IF something is true, THEN do this, ELSE do that!
# It's like having a smart robot that can choose what to do! 🤖

print("🤔 Welcome to If-Then-Else Demo!")
print("=" * 40)

# ===================
# 🌤️ SIMPLE IF STATEMENTS
# ===================
print("\n🌤️ SIMPLE IF STATEMENTS - Basic decisions!")
print("-" * 30)

# Let's check the weather
temperature = 25

print(f"Today's temperature is {temperature}°C")

if temperature > 30:
    print("It's hot! Time for the beach! 🏖️")

if temperature < 10:
    print("Brrr! It's cold! Get a jumper! 🧥")

if temperature >= 20 and temperature <= 30:
    print("Perfect weather for playing outside! ⚽")

# ===================
# ⚖️ IF-ELSE STATEMENTS - Two choices
# ===================
print("\n⚖️ IF-ELSE STATEMENTS - Choose between two options!")
print("-" * 30)

# Check if someone can drive
age = 17

print(f"You are {age} years old.")

if age >= 18:
    print("You can get a driver's license! 🚗")
else:
    print("You need to wait a bit longer to drive! 🚶‍♂️")

# Check game score
score = 85

print(f"Your game score is {score}")

if score >= 90:
    print("Excellent! You're a champion! 🏆")
else:
    print("Good try! Keep practicing! 💪")

# ===================
# 🏗️ IF-ELIF-ELSE STATEMENTS - Multiple choices
# ===================
print("\n🏗️ IF-ELIF-ELSE STATEMENTS - Multiple options!")
print("-" * 30)

# Grade checker
test_score = 78

print(f"Your test score is {test_score}")

if test_score >= 90:
    print("Grade: A - Outstanding! 🌟")
elif test_score >= 80:
    print("Grade: B - Well done! 👍")
elif test_score >= 70:
    print("Grade: C - Good effort! 👌")
elif test_score >= 60:
    print("Grade: D - Keep trying! 💪")
else:
    print("Grade: F - Let's study more! 📚")

# ===================
# 🎮 INTERACTIVE DECISION MAKING
# ===================
print("\n🎮 INTERACTIVE DECISION MAKING - You choose!")
print("-" * 30)

# Let's make decisions based on user input!
print("Welcome to the Decision Game!")

user_name = input("What's your name? ")
print(f"G'day {user_name}!")

# Ask about their favorite season
favorite_season = input("What's your favorite season (summer/winter/spring/autumn)? ").lower()

if favorite_season == "summer":
    print("Summer is bonzer! Time for swimming and BBQs! 🏊‍♂️🔥")
elif favorite_season == "winter":
    print("Winter is cozy! Perfect for hot chocolate and warm blankets! ☕🛋️")
elif favorite_season == "spring":
    print("Spring is beautiful! Flowers blooming everywhere! 🌸🦋")
elif favorite_season == "autumn":
    print("Autumn is lovely! Pretty leaves and cool weather! 🍂🍃")
else:
    print("That's not a season I know, but I bet it's nice! 🤷‍♂️")

# ===================
# 🔢 NUMBER GUESSING DECISION GAME
# ===================
print("\n🔢 NUMBER GUESSING DECISION GAME!")
print("-" * 30)

# The computer picks a number
secret_number = 7
print("I'm thinking of a number between 1 and 10...")

# Get the user's guess
guess = int(input("What's your guess? "))

if guess == secret_number:
    print("🎉 Amazing! You guessed it perfectly!")
    print("You're a mind reader! 🔮")
elif guess < secret_number:
    print("📈 Your guess is too low!")
    print(f"The secret number was {secret_number}")
elif guess > secret_number:
    print("📉 Your guess is too high!")
    print(f"The secret number was {secret_number}")

print("Thanks for playing! 🎮")

# ===================
# 🧠 COMPLEX DECISIONS - Multiple conditions
# ===================
print("\n🧠 COMPLEX DECISIONS - Combining conditions!")
print("-" * 30)

# Adventure game scenario
has_key = True
has_torch = False
door_locked = True

print("🏰 You're at a castle door!")
print(f"You have a key: {has_key}")
print(f"You have a torch: {has_torch}")
print(f"The door is locked: {door_locked}")

if has_key and door_locked:
    print("🔓 You unlock the door with your key!")
    if has_torch:
        print("🔦 Your torch lights the way inside!")
        print("You safely explore the castle! 🏰✨")
    else:
        print("🌑 It's very dark inside without a torch!")
        print("Maybe come back when you find some light! 💡")
elif not door_locked:
    print("🚪 The door is already open! You walk right in!")
else:
    print("🔒 The door is locked and you don't have a key!")
    print("You'll need to find another way in! 🤔")

print("\n" + "=" * 40)
print("🎉 Great job learning about decisions!")
print("🤔 IF: Check if something is true")
print("⚖️ ELSE: What to do if it's false")
print("🏗️ ELIF: Check multiple different conditions")
print("🧠 Decisions make your programs smart! 🤖")