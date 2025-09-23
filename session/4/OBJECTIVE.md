# Module 4 - Reading Files and Data Structures

## Learning Objective

In this module, students will learn how to **read and process data from external files** in Python, specifically using configuration files (`.ini` format) to create structured, data-driven applications. This is the foundation for building complex, maintainable programs.

## What You'll Learn

### 📁 File I/O Operations
- How to read external data files using Python's `configparser` library
- Understanding the `.ini` file format for storing structured configuration data
- Loading and parsing text-based data files into Python data structures

### 🔧 Data Processing Skills
- Converting file content into Python dictionaries and lists
- Processing comma-separated values within configuration files
- Handling different data types (strings, lists, None values)
- Organizing complex game data in separate files

### 🏗️ Program Architecture
- Separating code logic from data content for better organization
- Creating reusable functions for data loading (`load_graph_from_ini`, `load_stories`)
- Building data-driven applications that can be easily modified without changing code

## Key Programming Concepts

1. **File I/O (Input/Output)**: Reading external files safely and efficiently
2. **Data Structures**: Using dictionaries and lists to organize complex information
3. **Configuration Management**: Storing application data in external files
4. **Data Parsing**: Converting text-based formats into usable Python objects
5. **Code Organization**: Creating maintainable, modular programs

## Adventure Story Theme

🌲 **The Enchanted Forest Quest**: Students create a magical adventure game where heroes collect special items (magic rope, silver key, golden coin) to unlock new areas and ultimately save the Enchanted Forest!

## Core Files and Structure

### Configuration Files
- **`data.ini`**: Contains the game structure (locations, connections, requirements, rewards)
- **`stories.ini`**: Contains the narrative content for each location

### Python Files
- **`main.py`**: Demonstrates loading and displaying the data structures
- **`write-file.py`**: Shows how to generate content using AI and save it back to files
- **`support/build-readme.py`**: Utility to generate documentation from data
- **`support/path-finder.py`**: Advanced tool to analyze game paths and validate structure

## How It Works

The module demonstrates the complete cycle of file-based data management:

1. **Data Loading**: Read structured data from `.ini` files into Python dictionaries
2. **Data Processing**: Parse and organize the information for program use
3. **Data Analysis**: Use support tools to validate and understand the data structure
4. **Data Generation**: Create new content and save it back to files

## Real-World Applications

This module teaches essential skills used in:
- **Game Development**: Managing game assets, levels, and configuration
- **Web Applications**: Loading settings, content, and user data
- **Data Analysis**: Processing CSV files, configuration files, and structured data
- **System Administration**: Managing application configurations and settings
- **Scientific Computing**: Loading datasets and experimental parameters

## Programming Skills Developed

- **File handling** with proper error management
- **Data structure design** for complex applications
- **Configuration file formats** and parsing techniques
- **Modular programming** with reusable functions
- **Data validation** and integrity checking
- **Documentation generation** from code and data

By the end of this module, students will understand how to build flexible, data-driven applications that separate content from code, making their programs easier to maintain, extend, and share with others.