
"""
🦘 AUSTRALIAN ADVENTURES - LEARNING FUNCTIONS! 🐨

G'day mate! Let's learn about FUNCTIONS in Python!
Functions are like recipes - they do a job when you ask them to!
"""

# 🌟 WHAT IS A FUNCTION?
# A function is a block of code that does a special job
# You can use it over and over again!

# 🦘 EXAMPLE 1: A Simple Kangaroo Jump Function
def kangaroo_jump():
    """This function makes a kangaroo jump!"""
    print("🦘 Boing! The kangaroo jumped!")

# Let's use our function!
print("=== KANGAROO JUMPS ===")
kangaroo_jump()
kangaroo_jump()
kangaroo_jump()
print()


# 🐨 EXAMPLE 2: Functions with INPUTS (called parameters)
def greet_koala(name):
    """This function says hello to a koala by name!"""
    print(f"🐨 G'day {name}! Want some eucalyptus leaves?")

print("=== GREETING KOALAS ===")
greet_koala("Matilda")
greet_koala("Bruce")
greet_koala("Sheila")
print()


# 🏖️ EXAMPLE 3: Functions that RETURN something
def count_beach_items(shells, starfish):
    """This function counts items at the beach!"""
    total = shells + starfish
    return total

print("=== BEACH TREASURE ===")
my_shells = 5
my_starfish = 3
total_treasures = count_beach_items(my_shells, my_starfish)
print(f"🐚 I found {my_shells} shells and ⭐ {my_starfish} starfish!")
print(f"🏖️ That's {total_treasures} treasures total!")
print()


# 🦎 EXAMPLE 4: Multiple parameters
def aussie_animal_sound(animal, sound):
    """This function tells us what sound an animal makes!"""
    print(f"{animal} says: {sound}!")

print("=== ANIMAL SOUNDS ===")
aussie_animal_sound("🦎 Lizard", "Scuttle scuttle")
aussie_animal_sound("🦜 Kookaburra", "Kook-kook-kook-ka-ka-ka")
aussie_animal_sound("🐊 Crocodile", "SNAP")
aussie_animal_sound("🦘 Kangaroo", "Chortle chortle")
print()


# 🍪 EXAMPLE 5: Making Tim Tams (Australian biscuits!)
def make_tim_tams(how_many):
    """This function makes delicious Tim Tam biscuits!"""
    print(f"🍪 Making {how_many} Tim Tams...")
    print("   Mix chocolate 🍫")
    print("   Add biscuit layers 🥮")
    print("   Coat with more chocolate! 😋")
    return how_many * "🍪 "

print("=== TIM TAM FACTORY ===")
my_tim_tams = make_tim_tams(5)
print(f"Done! Here they are: {my_tim_tams}")
print()


# 🌊 EXAMPLE 6: Surfing waves!
def go_surfing(wave_height, surfer_name):
    """This function checks if it's safe to surf!"""
    if wave_height < 3:
        return f"🏄 {surfer_name}, the waves are too small! Maybe later."
    elif wave_height <= 6:
        return f"🏄 Perfect waves {surfer_name}! Let's surf! 🌊"
    else:
        return f"⚠️ Too dangerous {surfer_name}! Waves are too big!"

print("=== SURFING AT BONDI BEACH ===")
print(go_surfing(2, "Riley"))
print(go_surfing(5, "Charlie"))
print(go_surfing(8, "Alex"))
print()


# 🎨 EXAMPLE 7: Let's make a birthday party!
def throw_aussie_party(birthday_kid, age):
    """This function throws an awesome Aussie birthday party!"""
    print(f"🎉 {birthday_kid}'s Aussie Birthday Party! 🎉")
    print(f"🎂 {birthday_kid} is turning {age} years old!")
    print("🎈 Decorating with kangaroo balloons...")

    # Sing happy birthday!
    for i in range(age):
        print("🎵 ", end="")
    print("\n🎁 Time for fairy bread and lamingtons!")

    return "🥳 Best party ever!"

print("=== BIRTHDAY TIME ===")
result = throw_aussie_party("Emma", 9)
print(result)
print()


# 🧮 EXAMPLE 8: Math helper - Counting cricket runs
def calculate_cricket_score(fours, sixes):
    """This function calculates your cricket score!"""
    four_runs = fours * 4
    six_runs = sixes * 6
    total = four_runs + six_runs
    print(f"🏏 You hit {fours} fours = {four_runs} runs")
    print(f"🏏 You hit {sixes} sixes = {six_runs} runs")
    return total

print("=== CRICKET SCORE ===")
my_score = calculate_cricket_score(3, 2)
print(f"🏆 Total score: {my_score} runs!")
print()


# 🌟 YOUR TURN!
# Try creating your own function below!
# Ideas:
# - A function that makes a platypus swim 🦆
# - A function that counts your favorite Australian animals
# - A function that makes vegemite toast 🍞

print("=" * 40)
print("🎓 YOU'VE LEARNED ABOUT FUNCTIONS! 🎓")
print("Remember:")
print("1️⃣ Functions do a special job")
print("2️⃣ You can give them information (parameters)")
print("3️⃣ They can give you back answers (return)")
print("4️⃣ You can use them over and over!")
print("=" * 40)