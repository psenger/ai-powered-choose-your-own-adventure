# 💬 INPUT AND OUTPUT - TALKING WITH THE COMPUTER! 💬
#
# Programs need to talk with people! 
# INPUT = Getting information FROM the user
# OUTPUT = Showing information TO the user
# It's like having a conversation with your computer! 🤖

print("💬 Welcome to Input and Output Demo!")
print("=" * 40)

# ===================
# 📢 OUTPUT - Showing information to the user
# ===================
print("\n📢 OUTPUT - Computer talking to YOU!")
print("-" * 30)

# The print() function is like the computer's voice!
print("Hello! I'm your computer speaking!")
print("I can show you text, numbers, and more!")

# You can print different types of information
name = "Alex"
age = 11
height = 4.5

print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height} feet")

# You can make your output look fancy!
print("*" * 25)
print("* Welcome to our game! *")
print("*" * 25)

# ===================
# 📥 INPUT - Getting information from the user
# ===================
print("\n📥 INPUT - YOU talking to the computer!")
print("-" * 30)

# The input() function is like the computer's ears!
print("Now it's your turn to talk to me!")

# Get the user's name
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

# Get their favorite color
favorite_color = input("What's your favorite color? ")
print(f"Cool! {favorite_color} is a bonzer color!")

# Get their age (this comes in as text, so we need to convert it)
user_age_text = input("How old are you? ")
user_age = int(user_age_text)  # Convert text to number
print(f"Wow! {user_age} is a great age!")

# ===================
# 🎮 INTERACTIVE DEMO - Putting it all together!
# ===================
print("\n🎮 INTERACTIVE DEMO - Let's chat!")
print("-" * 30)

# Let's have a proper conversation!
print("Let me ask you some questions...")

# Question 1
pet_name = input("Do you have a pet? What's their name? ")
print(f"That's awesome! {pet_name} sounds like a great pet!")

# Question 2  
favorite_subject = input("What's your favorite subject at school? ")
print(f"{favorite_subject} is brilliant! Learning is so much fun!")

# Question 3
dream_job = input("What do you want to be when you grow up? ")
print(f"Being a {dream_job} would be amazing! You can do anything!")

# ===================
# 🧮 MATHEMATICAL INPUT - Working with numbers
# ===================
print("\n🧮 MATHEMATICAL INPUT - Let's do some maths!")
print("-" * 30)

# Get two numbers from the user
print("Let's add two numbers together!")
first_number = input("Give me your first number: ")
second_number = input("Give me your second number: ")

# Convert them from text to actual numbers
num1 = int(first_number)
num2 = int(second_number)

# Do the calculation
result = num1 + num2

# Show the result
print(f"{num1} + {num2} = {result}")
print("Maths is magic! ✨")

print("\n" + "=" * 40)
print("🎉 Great job with input and output!")
print("📢 OUTPUT: Computer shows you information")
print("📥 INPUT: You give the computer information") 
print("💬 Together they make conversations possible!")