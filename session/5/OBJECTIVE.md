# Module 5 - Calling AI APIs with Fallback

## Learning Objective

In this module, students will learn how to **integrate AI services** into their Python programs by making API calls to external AI systems (Ollama), with smart fallback strategies when the AI service is unavailable.

## What You'll Learn

### 🤖 AI Integration
- How to make HTTP requests to AI APIs using the `requests` library
- Understanding JSON payloads and API communication
- Working with AI language models to generate dynamic content

### 🔧 Technical Skills
- Making POST requests to external web services
- Handling API responses and error conditions
- Implementing fallback mechanisms for robust applications
- Using environment configuration for API endpoints

### 🎮 Game Features
- **Dynamic story generation** powered by AI (primary method)
- **Fallback to pre-written stories** when AI is unavailable (backup method)
- Complex prompt engineering for child-appropriate content
- Real-time story adaptation based on game state

## Key Programming Concepts

1. **API Integration**: Making HTTP requests to external services
2. **Error Handling**: Managing network failures and timeouts gracefully
3. **Fallback Strategies**: Ensuring your program works even when external services fail
4. **JSON Communication**: Sending and receiving structured data

## Adventure Story Theme

🌲 **The Enchanted Forest Quest**: Guide young adventurers through a magical forest where they must collect special items (magic rope, silver key, golden coin) to unlock new areas and ultimately save the Enchanted Forest by reaching the Rainbow Reflection Pool!

## How It Works

The game demonstrates two approaches to content delivery:

1. **Primary**: AI-generated stories using Ollama API calls
   - Sends prompts to a local AI service
   - Gets unique, dynamic responses each time
   - Adapts stories based on current game state

2. **Fallback**: Pre-written stories from files
   - Reads backup stories from `stories.ini`
   - Ensures the game always works, even offline
   - Provides consistent, tested content

## Real-World Applications

This module teaches essential programming skills used in:
- Modern web applications that integrate AI services
- Building resilient software with backup systems
- API-driven development and microservices
- Chatbots and interactive AI applications

By the end of this module, students will understand how to make their programs smarter by incorporating AI while ensuring they remain reliable through proper error handling and fallback mechanisms.