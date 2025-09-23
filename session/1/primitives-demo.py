# 🐍 PYTHON PRIMITIVES - THE BUILDING BLOCKS! 🐍
#
# Welcome to your first Python adventure! 
# Today we're learning about PRIMITIVES - the basic building blocks of all programs!
# Think of them like LEGO blocks - simple pieces that build amazing things! 🧱

print("🎮 Welcome to Python Primitives Demo!")
print("=" * 40)

# ===================
# 📝 STRINGS - TEXT AND WORDS
# ===================
print("\n📝 STRINGS - Working with text and words!")
print("-" * 30)

# A string is text wrapped in quotes - like writing a note!
player_name = "Sarah"
favorite_food = "lamingtons"
greeting_message = "G'day mate!"

print(f"Player name: {player_name}")
print(f"Favorite food: {favorite_food}")
print(f"Greeting: {greeting_message}")

# You can JOIN strings together (called concatenation)
full_message = greeting_message + " Want some " + favorite_food + "?"
print(f"Combined message: {full_message}")

# Strings have special powers! Let's see some:
print(f"Player name in UPPERCASE: {player_name.upper()}")
print(f"Player name in lowercase: {player_name.lower()}")
print(f"Length of player name: {len(player_name)} letters")

# ===================
# 🔢 NUMBERS - MATHS AND COUNTING
# ===================
print("\n🔢 NUMBERS - Doing maths and counting!")
print("-" * 30)

# Integers (whole numbers) - like counting sheep!
player_age = 10
score = 85
lives_remaining = 3

print(f"Player age: {player_age}")
print(f"Game score: {score}")
print(f"Lives remaining: {lives_remaining}")

# You can do maths with numbers!
total_points = score + 15  # Addition
remaining_time = 60 - 23   # Subtraction
double_score = score * 2   # Multiplication
half_age = player_age / 2  # Division

print(f"Total points after bonus: {total_points}")
print(f"Time remaining: {remaining_time} seconds")
print(f"Double score would be: {double_score}")
print(f"Half the player's age: {half_age}")

# Floating point numbers (decimals) - for precise measurements!
temperature = 23.5
price = 4.99
success_rate = 87.3

print(f"Temperature: {temperature}°C")
print(f"Price: ${price}")
print(f"Success rate: {success_rate}%")

# ===================
# ✅❌ BOOLEANS - TRUE OR FALSE
# ===================
print("\n✅❌ BOOLEANS - True or False!")
print("-" * 30)

# Booleans are like light switches - ON (True) or OFF (False)
is_game_over = False
player_has_key = True
is_raining = False
found_treasure = True

print(f"Game over? {is_game_over}")
print(f"Player has key? {player_has_key}")
print(f"Is it raining? {is_raining}")
print(f"Found treasure? {found_treasure}")

# You can create booleans by comparing things!
age_check = player_age >= 10        # Is age 10 or more?
high_score = score > 100            # Is score more than 100?
perfect_temperature = temperature == 25.0  # Is temperature exactly 25?

print(f"Age 10 or more? {age_check}")
print(f"High score (>100)? {high_score}")
print(f"Perfect temperature (25°)? {perfect_temperature}")

print("\n" + "=" * 40)
print("🎉 You've learned about Python's basic building blocks!")
print("📝 Strings for text")
print("🔢 Numbers for maths") 
print("✅ Booleans for true/false")
print("These are the LEGO blocks of programming! 🧱")