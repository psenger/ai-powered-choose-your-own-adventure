# 🔄 LOOPS - DOING THINGS AGAIN AND AGAIN! 🔄
#
# Sometimes you want to do the same thing multiple times!
# Instead of copying code, we use LOOPS - they're like magic spells
# that make the computer repeat actions! ✨

print("🔄 Welcome to Loops Demo!")
print("=" * 40)

# ===================
# 📊 FOR LOOPS - Counting and repeating
# ===================
print("\n📊 FOR LOOPS - Repeat a specific number of times!")
print("-" * 30)

# Count from 1 to 5
print("Counting from 1 to 5:")
for number in range(1, 6):  # range(1, 6) gives us 1, 2, 3, 4, 5
    print(f"Number: {number}")

print()

# Let's count down like a rocket launch!
print("🚀 Rocket launch countdown:")
for countdown in range(5, 0, -1):  # Count backwards from 5 to 1
    print(f"{countdown}...")
print("🚀 BLAST OFF! 🚀")

print()

# Print stars to make a pattern
print("Making a star pattern:")
for i in range(1, 6):
    stars = "⭐" * i  # Multiply the star emoji by the number
    print(stars)

# ===================
# 📝 FOR LOOPS WITH LISTS - Going through collections
# ===================
print("\n📝 FOR LOOPS WITH LISTS - Go through collections!")
print("-" * 30)

# List of favorite foods
favorite_foods = ["pizza", "ice cream", "chocolate", "lamingtons", "fairy bread"]

print("My favorite foods are:")
for food in favorite_foods:
    print(f"- {food} (yum!) 😋")

print()

# List of friends
friends = ["Sarah", "Jake", "Emma", "Liam"]

print("Saying hello to all my friends:")
for friend in friends:
    print(f"G'day {friend}! 👋")

# ===================
# 🔁 WHILE LOOPS - Keep going until something happens
# ===================
print("\n🔁 WHILE LOOPS - Keep going until condition is met!")
print("-" * 30)

# Count up while a condition is true
number = 1
print("Counting while number is less than 5:")
while number < 5:
    print(f"Number is: {number}")
    number = number + 1  # This is VERY important! Without this, loop goes forever!

print("Loop finished!")

print()

# Simple guessing game with while loop
secret_password = "python"
attempts = 0
max_attempts = 3

print("🔐 Password guessing game!")
print(f"You have {max_attempts} attempts to guess the password.")

# This is a pretend game - we'll just show how it would work
guesses = ["hello", "password", "python"]  # Pretend user guesses

for guess in guesses:  # Simulate user input
    attempts = attempts + 1
    print(f"Attempt {attempts}: You guessed '{guess}'")
    
    if guess == secret_password:
        print("🎉 Correct! You cracked the code!")
        break  # Exit the loop early
    elif attempts >= max_attempts:
        print("🔒 Sorry, you're out of attempts!")
        print(f"The password was '{secret_password}'")
        break
    else:
        print("❌ Wrong password, try again!")

# ===================
# 🎮 INTERACTIVE LOOP EXAMPLE
# ===================
print("\n🎮 INTERACTIVE LOOP EXAMPLE!")
print("-" * 30)

# Let's collect information from the user multiple times
print("Tell me about your hobbies! (Type 'done' when finished)")

hobbies = []  # Empty list to store hobbies
hobby_count = 0

# In a real program, this would be:
# while True:
#     hobby = input("What's one of your hobbies? ")
#     if hobby.lower() == "done":
#         break
#     hobbies.append(hobby)
#     hobby_count += 1

# For this demo, let's pretend the user entered some hobbies
demo_hobbies = ["reading", "gaming", "drawing", "done"]

for hobby_input in demo_hobbies:
    if hobby_input.lower() == "done":
        print("Thanks for sharing!")
        break
    else:
        hobbies.append(hobby_input)
        hobby_count += 1
        print(f"Added '{hobby_input}' to your hobbies list!")

print(f"\nYou told me about {hobby_count} hobbies:")
for i, hobby in enumerate(hobbies, 1):  # enumerate gives us numbers starting from 1
    print(f"{i}. {hobby}")

# ===================
# 🌟 NESTED LOOPS - Loops inside loops!
# ===================
print("\n🌟 NESTED LOOPS - Loops inside other loops!")
print("-" * 30)

# Create a simple grid pattern
print("Making a grid with loops:")
for row in range(1, 4):  # 3 rows
    for column in range(1, 6):  # 5 columns
        print("🟦", end=" ")  # end=" " means don't go to new line
    print()  # Now go to new line after each row

print()

# Multiplication table (just 1-3 to keep it simple)
print("Mini multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} × {j} = {result}")
    print()  # Blank line between each number's table

# ===================
# 🎯 PRACTICAL LOOP EXAMPLES
# ===================
print("\n🎯 PRACTICAL LOOP EXAMPLES!")
print("-" * 30)

# Calculate total scores
game_scores = [85, 92, 78, 96, 88]
total_score = 0

print("Your game scores:")
for score in game_scores:
    print(f"Score: {score}")
    total_score = total_score + score

average_score = total_score / len(game_scores)
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.1f}")

print()

# Find the highest score
highest_score = 0
for score in game_scores:
    if score > highest_score:
        highest_score = score

print(f"Your highest score was: {highest_score} 🏆")

# ===================
# 🎪 FUN LOOP PATTERNS
# ===================
print("\n🎪 FUN LOOP PATTERNS!")
print("-" * 30)

# Make a triangle
print("Triangle pattern:")
for i in range(1, 6):
    spaces = " " * (5 - i)  # Spaces for centering
    stars = "⭐" * i
    print(spaces + stars)

print()

# Make a Christmas tree (sort of!)
print("Christmas tree pattern:")
for i in range(1, 5):
    spaces = " " * (4 - i)
    stars = "🌲" * i
    print(spaces + stars)

print()

# Count vowels in a word
word = "programming"
vowels = "aeiou"
vowel_count = 0

print(f"Counting vowels in the word '{word}':")
for letter in word:
    if letter.lower() in vowels:
        print(f"'{letter}' is a vowel!")
        vowel_count += 1

print(f"Total vowels found: {vowel_count}")

print("\n" + "=" * 40)
print("🎉 Amazing work with loops!")
print("📊 FOR loops: Repeat a specific number of times")
print("🔁 WHILE loops: Keep going until something happens")
print("🌟 NESTED loops: Loops inside other loops")
print("🔄 Loops save you from writing the same code over and over! ✨")