# 📁 Key Files Reference for All Modules

This document identifies the most important files for each module's learning objectives.

## 🧱 Module 1 - Programming Primitives and Fundamentals

### **PRIMARY LEARNING FILES** ⭐ (Students must complete these):

1. **`primitives-demo.py`** - **MOST IMPORTANT**
   - Strings, numbers, booleans, and variables
   - Foundation for all other programming concepts

2. **`input-output-demo.py`** - **ESSENTIAL** 
   - User interaction with `input()` and `print()`
   - Data conversion between text and numbers

3. **`if-else-demo.py`** - **CORE CONCEPT**
   - Decision-making with if-then-else statements
   - Boolean logic and comparisons

4. **`loops-demo.py`** - **FUNDAMENTAL**
   - For loops and while loops
   - Repetition and iteration patterns

### **FOUNDATION FILES** (Optional warm-up):
- `hello-world.py` - Simplest possible program
- `ask-name.py` - Basic input introduction

---

## 🔧 Module 2 - Functions and Program Organization

### **PRIMARY LEARNING FILES** ⭐ (Students must complete these):

1. **`main.py`** - **MOST IMPORTANT**
   - Complete demonstration of all function types
   - Function definition, parameters, return values
   - `if __name__ == "__main__":` pattern
   - Professional program structure

2. **`input-output.py`** - **SUPPORTING**
   - Simple linear programming approach
   - Shows the difference between structured and unstructured code

### **LEARNING OBJECTIVES**:
- Functions as reusable code machines
- Parameters for input, return values for output
- Program organization and modularity
- `__name__` pattern for main program control

---

## 🌐 Module 3 - AI API Integration

### **PRIMARY LEARNING FILES** ⭐ (Students must complete these):

1. **`main.py`** - **MOST IMPORTANT**
   - Complete AI integration with Ollama
   - HTTP requests with `requests` library
   - System prompts vs user prompts
   - Error handling and graceful fallbacks
   - Master Oogway character demonstration

2. **`test-ollama.py`** - **ESSENTIAL TESTING**
   - Connection testing and service validation
   - Model discovery and availability checking
   - Diagnostic reporting and troubleshooting
   - Professional testing infrastructure

### **LEARNING OBJECTIVES**:
- HTTP API calls to external services
- JSON payload construction and response handling
- Network error management and timeouts
- AI prompt engineering and character development

---

## 📁 Module 4 - File I/O and Data Structures

### **PRIMARY LEARNING FILES** ⭐ (Students must complete these):

1. **`main.py`** - **MOST IMPORTANT**
   - Loading data from `.ini` files with `configparser`
   - Converting file data to Python dictionaries
   - Displaying structured data organization

### **SUPPORTING FILES**:

2. **`data.ini`** - **ESSENTIAL DATA**
   - Game structure: locations, connections, requirements, rewards
   - Demonstrates `.ini` file format for configuration

3. **`stories.ini`** - **CONTENT DATA**
   - Pre-written story content for each location
   - Backup content for when AI is unavailable

4. **`write-file.py`** - **ADVANCED (Optional)**
   - AI-powered story generation
   - Saving generated content back to files
   - Demonstrates AI + file operations combined

### **UTILITY FILES** (Advanced students):
- `support/build-readme.py` - Documentation generation
- `support/path-finder.py` - Game path analysis and validation

### **LEARNING OBJECTIVES**:
- File reading with `configparser`
- Data-driven programming (separate code from content)
- Dictionary and list data structures
- Configuration file management

---

## 🎮 Module 5 - Complete Application with AI Fallback

### **PRIMARY LEARNING FILES** ⭐ (Students must complete these):

1. **`main.py`** - **MOST IMPORTANT**
   - Complete choose-your-own-adventure game
   - AI integration for dynamic story generation
   - Fallback to file-based stories when AI unavailable
   - Inventory system and item-based progression
   - User choice handling and game state management

### **SUPPORTING FILES**:

2. **`data.ini`** - **GAME STRUCTURE**
   - Same as Module 4, but now used in complete game
   - Demonstrates how file data drives game logic

3. **`stories.ini`** - **FALLBACK CONTENT**
   - Pre-written stories used when AI is unavailable
   - Ensures game always works regardless of AI status

### **LEARNING OBJECTIVES**:
- Combining all previous concepts in one application
- AI integration with robust fallback strategies
- Complex game state management
- Error handling for external dependencies
- Real-world application architecture

---

## 📚 Learning Progression Summary

### **Recommended Study Order**:

1. **Module 1**: Learn primitives → `primitives-demo.py`, `input-output-demo.py`, `if-else-demo.py`, `loops-demo.py`

2. **Module 2**: Learn functions → `main.py` (focus on function organization)

3. **Module 3**: Learn AI APIs → `main.py` (AI integration), `test-ollama.py` (testing)

4. **Module 4**: Learn file I/O → `main.py` (data loading), `data.ini` & `stories.ini` (file formats)

5. **Module 5**: Complete application → `main.py` (everything combined)

### **Skills Building Path**:
```
Module 1: Primitives & Logic
    ↓
Module 2: Functions & Organization  
    ↓
Module 3: External APIs & AI
    ↓
Module 4: File Operations & Data
    ↓
Module 5: Complete Applications
```

Each module builds on the previous ones, with Module 5 combining all concepts into a professional-quality application that demonstrates real-world programming skills.