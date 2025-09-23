# Session 2 - What is a Function

## Overview

This module introduces students to **functions** - the fundamental building blocks of programming. Students learn to create reusable code components, organize programs effectively, and build the foundation for all future programming concepts through engaging, child-friendly examples.

## Program Flow and Architecture

### Simple Script Flow (input-output.py)

```
SIMPLE PROGRAM EXECUTION
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ Linear Script Execution                                         │
│                                                                 │
│  Step 1: Welcome Messages                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ print("🎮 Welcome to the Adventure Game!")              │   │
│  │ print("You are standing at the edge of a dark forest.") │   │
│  │ print("=" * 30)  # Decorative line                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 2: User Input Collection                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ player_name = input("What is your name, brave adventurer?") │
│  │  ├─ Display prompt to user                              │   │
│  │  ├─ Wait for user to type response                     │   │
│  │  ├─ Store response in player_name variable             │   │
│  │  └─ Continue execution                                  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 3: Personalized Response                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ print(f"\nHello {player_name}! Get ready for...")       │   │
│  │  ├─ Use f-string formatting                            │   │
│  │  ├─ Insert player_name into message                    │   │
│  │  └─ Display personalized greeting                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 4: Program Completion                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ # TODO: Add the next part of the adventure              │   │
│  │ # Program ends here (for now)                          │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Function-Based Program Flow (main.py)

```
FUNCTION-BASED PROGRAM EXECUTION
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ Function Definitions Phase                                      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ def say_hello():                                        │   │
│  │     # Function body defines what happens when called    │   │
│  │     print("G'day mate! Welcome to our awesome game!")  │   │
│  │     print("Hope you're ready for an adventure!")       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ def greet_player(player_name):                          │   │
│  │     # Parameter: player_name acts like a variable      │   │
│  │     print(f"Hello {player_name}! Ready to play?")      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ def add_numbers(first_number, second_number):           │   │
│  │     # Return value: function gives back a result       │   │
│  │     result = first_number + second_number               │   │
│  │     return result                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ def ask_favorite_color():                               │   │
│  │     # Interactive function: gets user input            │   │
│  │     color = input("What's your favorite color? ")      │   │
│  │     return color                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ Function Testing Phase                                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ say_hello()  # Call function with no parameters        │   │
│  │ greet_player("Sarah")  # Call with string argument     │   │
│  │ my_answer = add_numbers(5, 3)  # Store return value    │   │
│  │ their_color = ask_favorite_color()  # Interactive call │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ Main Program Execution (if __name__ == "__main__")             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ if __name__ == "__main__":                              │   │
│  │     # This runs only when file is executed directly    │   │
│  │     say_hello()                                         │   │
│  │     player_name = input("What's your name? ")          │   │
│  │     greet_player(player_name)                           │   │
│  │     answer = add_numbers(10, 25)                        │   │
│  │     color = ask_favorite_color()                        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Function Anatomy and Types

### Function Structure Breakdown

```
Function Anatomy
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  def function_name(parameter1, parameter2):                     │
│   │      │              │           │                          │
│   │      │              └─────┬─────┘                          │
│   │      │                    │                                │
│   │      │                    └─ Parameters (inputs)           │
│   │      │                                                     │
│   │      └─ Function name (what to call it)                    │
│   │                                                             │
│   └─ def keyword (defines a function)                          │
│                                                                 │
│      # Function body (what it does)                            │
│      result = parameter1 + parameter2                          │
│      return result  # Return value (output)                    │
│                      │                                         │
│                      └─ return keyword gives back a value      │
└─────────────────────────────────────────────────────────────────┘
```

### Four Types of Functions Demonstrated

```
Function Types Overview
┌─────────────────────────────────────────────────────────────────┐
│ Type 1: Simple Action Functions                                │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ def say_hello():                                            │ │
│ │     print("G'day mate!")                                   │ │
│ │                                                             │ │
│ │ Input:  None                                                │ │
│ │ Output: None (just performs actions)                       │ │
│ │ Use:    Reusable blocks of code                            │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Type 2: Parameterized Functions                               │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ def greet_player(player_name):                              │ │
│ │     print(f"Hello {player_name}!")                         │ │
│ │                                                             │ │
│ │ Input:  String (player's name)                             │ │
│ │ Output: None (but uses input for customization)            │ │
│ │ Use:    Flexible, reusable code                            │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Type 3: Calculation Functions                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ def add_numbers(first_number, second_number):               │ │
│ │     result = first_number + second_number                   │ │
│ │     return result                                           │ │
│ │                                                             │ │
│ │ Input:  Two numbers                                         │ │
│ │ Output: Calculated result                                   │ │
│ │ Use:    Mathematical operations and data processing        │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Type 4: Interactive Functions                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ def ask_favorite_color():                                   │ │
│ │     color = input("What's your favorite color? ")          │ │
│ │     return color                                            │ │
│ │                                                             │ │
│ │ Input:  None (but gets user input internally)              │ │
│ │ Output: User's response                                     │ │
│ │ Use:    User interaction and data collection               │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Function Call Flow and Data Movement

### Function Call Process

```
Function Call and Execution Flow
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ 1. Function Call Initiated                                     │
│    my_answer = add_numbers(5, 3)                               │
│                     │       │                                  │
│                     └───┬───┘                                  │
│                         │                                      │
│                    Arguments passed                            │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ 2. Function Definition Located                                  │
│    def add_numbers(first_number, second_number):                │
│                        │             │                         │
│                        └─────┬───────┘                         │
│                              │                                 │
│                         Parameters receive arguments           │
│                         first_number = 5                      │
│                         second_number = 3                     │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ 3. Function Body Executed                                      │
│    result = first_number + second_number                       │
│    result = 5 + 3                                             │
│    result = 8                                                 │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ 4. Return Value Sent Back                                      │
│    return result                                               │
│    return 8                                                    │
│            │                                                   │
│            └─ Value flows back to caller                       │
└─────────────────────────────────────────────────────────────────┘
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ 5. Assignment Completed                                        │
│    my_answer = 8                                               │
│                                                                │
│    The variable my_answer now contains the result             │
└─────────────────────────────────────────────────────────────────┘
```

## Program Entry Point Pattern

### Understanding `if __name__ == "__main__"`

```
Program Execution Context
┌─────────────────────────────────────────────────────────────────┐
│ When Python runs your file...                                  │
│                                                                 │
│ Scenario 1: Direct Execution                                   │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ $ python main.py                                            │ │
│ │                                                             │ │
│ │ Python sets: __name__ = "__main__"                         │ │
│ │                                                             │ │
│ │ if __name__ == "__main__":  # This is TRUE                 │ │
│ │     # Main program code runs                               │ │
│ │     print("Running main program!")                         │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ Scenario 2: Import by Another Program                          │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ # In another file:                                          │ │
│ │ import main                                                 │ │
│ │                                                             │ │
│ │ Python sets: __name__ = "main"                             │ │
│ │                                                             │ │
│ │ if __name__ == "__main__":  # This is FALSE                │ │
│ │     # Main program code DOES NOT run                       │ │
│ │     # Only function definitions are available              │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Security Guard Analogy

```
The __name__ Security Guard System
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│     🏢 Your Python Program Building                            │
│                                                                 │
│     ┌─────────────────────────────────┐                       │
│     │                                 │                       │
│     │  Functions Available to All     │                       │
│     │  (Public Library)               │                       │
│     │  ├─ say_hello()                │                       │
│     │  ├─ greet_player()             │                       │
│     │  ├─ add_numbers()              │                       │
│     │  └─ ask_favorite_color()       │                       │
│     │                                 │                       │
│     └─────────────────────────────────┘                       │
│                                                                 │
│     ┌─────────────────────────────────┐                       │
│     │                                 │                       │
│     │  🛡️ Security Guard               │                       │
│     │  if __name__ == "__main__":     │                       │
│     │                                 │                       │
│     │  ✅ Direct visitors allowed in   │                       │
│     │  ❌ Imported visitors stay out   │                       │
│     │                                 │                       │
│     └─────────────────────────────────┘                       │
│                                                                 │
│     ┌─────────────────────────────────┐                       │
│     │                                 │                       │
│     │  Main Program (Private Office)  │                       │
│     │  ├─ Interactive demos           │                       │
│     │  ├─ Test examples               │                       │
│     │  └─ Main application logic      │                       │
│     │                                 │                       │
│     └─────────────────────────────────┘                       │
└─────────────────────────────────────────────────────────────────┘
```

## Variable Scope and Data Flow

### Scope Visualization

```
Variable Scope in Functions
┌─────────────────────────────────────────────────────────────────┐
│ Global Scope (Outside Functions)                               │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ player_name = "Sarah"  # Global variable                   │ │
│ │ my_answer = None       # Available everywhere              │ │
│ │                                                             │ │
│ │ Function Scope (Inside Functions)                          │ │
│ │ ┌─────────────────────────────────────────────────────────┐ │ │
│ │ │ def greet_player(player_name):                          │ │ │
│ │ │     # Parameter 'player_name' is local to this function│ │ │
│ │ │     message = f"Hello {player_name}!"  # Local variable│ │ │
│ │ │     print(message)                                      │ │ │
│ │ │                                                         │ │ │
│ │ │     # Can read global variables (but avoid this)       │ │ │
│ │ │     # Cannot modify global variables without 'global'  │ │ │
│ │ └─────────────────────────────────────────────────────────┘ │ │
│ │                                                             │ │
│ │ ┌─────────────────────────────────────────────────────────┐ │ │
│ │ │ def add_numbers(first_number, second_number):           │ │ │
│ │ │     result = first_number + second_number  # Local     │ │ │
│ │ │     return result  # Send local variable out           │ │ │
│ │ │                                                         │ │ │
│ │ │     # 'result' doesn't exist outside this function     │ │ │
│ │ └─────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Learning Progression and Skills Development

### Module 2 Skills Ladder

```
Skills Development Progression
┌─────────────────────────────────────────────────────────────────┐
│ Level 4: Program Organization                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ ✅ Using __name__ == "__main__" pattern                     │ │
│ │ ✅ Creating modular, importable code                        │ │
│ │ ✅ Understanding program structure                          │ │
│ │ ✅ Writing professional-style code                          │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Level 3: Return Values and Data Flow                           │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ ✅ Functions that return calculated results                 │ │
│ │ ✅ Storing function outputs in variables                    │ │
│ │ ✅ Understanding data flow in and out of functions         │ │
│ │ ✅ Building calculator-style functions                      │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Level 2: Parameters and Input                                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ ✅ Functions that accept parameters                         │ │
│ │ ✅ Making functions flexible and customizable               │ │
│ │ ✅ Understanding argument passing                           │ │
│ │ ✅ Using multiple parameters                                │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Level 1: Basic Functions                                       │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ ✅ Understanding what functions are                         │ │
│ │ ✅ Defining simple functions with def                       │ │
│ │ ✅ Calling functions by name                                │ │
│ │ ✅ Writing reusable code blocks                             │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Real-World Function Applications

### Practical Examples and Analogies

```
Functions in Daily Life
┌─────────────────────────────────────────────────────────────────┐
│ Kitchen Appliances (Function Machines)                         │
│                                                                 │
│ Toaster Function:                    Coffee Maker Function:    │
│ ┌─────────────────────────┐         ┌─────────────────────────┐ │
│ │ Input: Bread slices     │         │ Input: Water + Grounds  │ │
│ │ Process: Heat and time  │         │ Process: Heat and brew  │ │
│ │ Output: Toast           │         │ Output: Coffee          │ │
│ │                         │         │                         │ │
│ │ def make_toast(bread):  │         │ def make_coffee(water): │ │
│ │     # heating process   │         │     # brewing process   │ │
│ │     return toasted_bread│         │     return hot_coffee   │ │
│ └─────────────────────────┘         └─────────────────────────┘ │
│                                                                 │
│ Calculator Function:                 ATM Function:              │
│ ┌─────────────────────────┐         ┌─────────────────────────┐ │
│ │ Input: Two numbers      │         │ Input: PIN + Amount     │ │
│ │ Process: Mathematical   │         │ Process: Verification   │ │
│ │ Output: Result          │         │ Output: Cash + Receipt  │ │
│ │                         │         │                         │ │
│ │ def add(a, b):          │         │ def withdraw(pin, amt): │ │
│ │     return a + b        │         │     # security check    │ │
│ └─────────────────────────┘         │     return cash         │ │
│                                     └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Code Quality and Best Practices

### Function Design Principles

```
Good Function Design Checklist
┌─────────────────────────────────────────────────────────────────┐
│ ✅ Single Responsibility                                        │
│    Each function should do ONE job well                        │
│    ❌ def do_everything():  # Too much!                        │
│    ✅ def greet_player():   # Just greeting                    │
│                                                                 │
│ ✅ Clear, Descriptive Names                                    │
│    Function names should explain what they do                  │
│    ❌ def func1():          # What does this do?               │
│    ✅ def ask_favorite_color():  # Crystal clear              │
│                                                                 │
│ ✅ Appropriate Parameters                                      │
│    Only ask for what you need                                  │
│    ❌ def greet(name, age, color, pet, food):  # Too many!    │
│    ✅ def greet(name):      # Just what's needed              │
│                                                                 │
│ ✅ Helpful Comments                                            │
│    Explain the purpose and any tricky parts                    │
│    ✅ # This function adds two numbers together                │
│    ✅ def add_numbers(first, second):                          │
│                                                                 │
│ ✅ Consistent Return Behavior                                  │
│    Always return the same type of thing                        │
│    ❌ Sometimes return string, sometimes number                │
│    ✅ Always return a number for math functions                │
└─────────────────────────────────────────────────────────────────┘
```

## Foundation for Future Learning

This module establishes essential programming foundations that enable:

- **Module 3**: Using functions to organize AI API calls and error handling
- **Module 4**: Creating functions to process file data and manage game state
- **Module 5**: Building complex game systems with multiple interacting functions
- **Advanced Programming**: Object-oriented programming, data structures, algorithms

Students learn that functions are the building blocks that make all complex programming possible - from simple calculations to advanced AI applications.