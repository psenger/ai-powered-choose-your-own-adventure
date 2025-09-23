# Session 3 - Talking to AI

## Overview

This module introduces students to **AI service integration** by teaching how to make HTTP API calls to external AI systems. Students learn to communicate with AI services like Ollama, handle network errors gracefully, and build robust applications that leverage artificial intelligence.

## Program Flow and Architecture

### Main Application Flow (main.py)

```
PROGRAM STARTUP
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ AI Conversation Demo - Master Oogway Character                  │
│                                                                 │
│  Step 1: Define AI Personality                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ system_prompt = """                                     │   │
│  │   You are Master Oogway, the wise old turtle...        │   │
│  │   [Character definition and speaking style]            │   │
│  │ """                                                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 2: Create User Query                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ user_prompt = """                                       │   │
│  │   Master Oogway, I'm trying to learn Python...         │   │
│  │   [Specific question about programming]                 │   │
│  │ """                                                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 3: Display Context                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Print introduction and user question                    │   │
│  │ Set stage for AI interaction                            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 4: Call AI Service                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ response = call_ollama(user_prompt, system_prompt)      │   │
│  │  ├─ Send HTTP request to Ollama API                    │   │
│  │  ├─ Handle response or errors                          │   │
│  │  └─ Return formatted response                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 5: Display Results                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Print AI response with character formatting             │   │
│  │ Provide engaging user experience                        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### AI API Call Flow (call_ollama function)

```
call_ollama(prompt, system_prompt)
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ HTTP API Request Process                                        │
│                                                                 │
│  Step 1: Build Request Payload                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ payload = {                                             │   │
│  │   "model": "llama3.1:8b",                              │   │
│  │   "prompt": user_prompt,                               │   │
│  │   "system": system_prompt,                             │   │
│  │   "stream": False,                                     │   │
│  │   "options": {                                         │   │
│  │     "temperature": 0.7,    # Creativity level         │   │
│  │     "top_p": 0.9,          # Response diversity       │   │
│  │     "max_tokens": 300      # Response length limit    │   │
│  │   }                                                    │   │
│  │ }                                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 2: Make HTTP Request                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ requests.post()                                         │   │
│  │  ├─ URL: http://localhost:11434/api/generate           │   │
│  │  ├─ Method: POST                                       │   │
│  │  ├─ Headers: Content-Type: application/json           │   │
│  │  ├─ Body: JSON payload                                 │   │
│  │  └─ Timeout: 30 seconds                               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Step 3: Handle Response                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SUCCESS (Status 200)        ERROR CONDITIONS            │   │
│  │ ┌─────────────────────┐    ┌─────────────────────────┐  │   │
│  │ │ Parse JSON response │    │ Connection Error        │  │   │
│  │ │ Extract 'response'  │    │ ├─ Ollama not running   │  │   │
│  │ │ Clean formatting    │    │ └─ Return friendly msg  │  │   │
│  │ │ Return AI text      │    │                         │  │   │
│  │ └─────────────────────┘    │ HTTP Error              │  │   │
│  │                            │ ├─ Status != 200        │  │   │
│  │                            │ └─ Return backup msg    │  │   │
│  │                            │                         │  │   │
│  │                            │ Timeout                 │  │   │
│  │                            │ ├─ Request > 30 sec     │  │   │
│  │                            │ └─ Return timeout msg   │  │   │
│  │                            └─────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Testing Infrastructure Flow (test-ollama.py)

### Comprehensive Service Testing Process

```
test-ollama.py Execution
   |
   v
┌─────────────────────────────────────────────────────────────────┐
│ Ollama Service Validation Suite                                 │
│                                                                 │
│  Phase 1: Connection Testing                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ test_ollama_connection()                                │   │
│  │  ├─ GET /api/version                                   │   │
│  │  ├─ Timeout: 5 seconds                                │   │
│  │  ├─ Check status code == 200                          │   │
│  │  ├─ Extract version information                       │   │
│  │  └─ Report connection status                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Phase 2: Model Discovery                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ list_available_models()                                 │   │
│  │  ├─ GET /api/tags                                      │   │
│  │  ├─ Parse models list                                  │   │
│  │  ├─ Display available models                           │   │
│  │  └─ Check for required models                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Phase 3: Generation Testing                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ test_simple_generation()                                │   │
│  │  ├─ POST /api/generate                                 │   │
│  │  ├─ Test prompt: "Tell me a short story..."           │   │
│  │  ├─ Validate response format                           │   │
│  │  ├─ Check generation quality                           │   │
│  │  └─ Report success/failure                             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Phase 4: Diagnostic Reporting                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ✅ Service status summary                               │   │
│  │ 📋 Version and configuration info                       │   │
│  │ 🤖 Available models list                                │   │
│  │ 🎯 Generation capability test                           │   │
│  │ 💡 Troubleshooting recommendations                      │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Error Handling Architecture

### Multi-Layer Error Management

```
Error Handling Strategy
┌─────────────────────────────────────────────────────────────────┐
│ Network Layer Errors                                           │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ ConnectionError                                             │ │
│ │ ├─ Ollama service not running                              │ │
│ │ ├─ Wrong URL or port                                       │ │
│ │ └─ Network connectivity issues                             │ │
│ │                                                             │ │
│ │ TimeoutError                                                │ │
│ │ ├─ Ollama taking too long to respond                       │ │
│ │ ├─ Model loading delays                                    │ │
│ │ └─ Heavy server load                                       │ │
│ │                                                             │ │
│ │ HTTPError                                                   │ │
│ │ ├─ 404: API endpoint not found                             │ │
│ │ ├─ 500: Internal server error                              │ │
│ │ └─ 503: Service unavailable                                │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ Application Layer Errors                                       │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ Empty Response                                              │ │
│ │ ├─ AI model returned blank output                          │ │
│ │ └─ Malformed JSON response                                 │ │
│ │                                                             │ │
│ │ Model Errors                                                │ │
│ │ ├─ Requested model not available                           │ │
│ │ ├─ Model loading failed                                    │ │
│ │ └─ Insufficient system resources                           │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ User Experience Layer                                          │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ Friendly Error Messages                                     │ │
│ │ ├─ "The AI storyteller is taking a nap! 😴"               │ │
│ │ ├─ "The magic is a bit wobbly right now! ✨"              │ │
│ │ └─ "Let's continue with a backup story! 📚"               │ │
│ │                                                             │ │
│ │ Graceful Degradation                                        │ │
│ │ ├─ Continue program execution                               │ │
│ │ ├─ Provide alternative content                              │ │
│ │ └─ Maintain engaging user experience                       │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## API Communication Protocol

### HTTP Request/Response Cycle

```
Client (Python App)                    Server (Ollama API)
┌─────────────────┐                    ┌─────────────────┐
│                 │                    │                 │
│  1. Build JSON  │                    │                 │
│     Payload     │                    │                 │
│                 │                    │                 │
│  2. HTTP POST   │─────────────────▶  │  3. Receive     │
│     Request     │                    │     Request     │
│                 │                    │                 │
│                 │                    │  4. Load Model  │
│                 │                    │     (if needed) │
│                 │                    │                 │
│                 │                    │  5. Generate    │
│                 │                    │     Response    │
│                 │                    │                 │
│  7. Parse JSON  │  ◀─────────────────│  6. Send JSON   │
│     Response    │                    │     Response    │
│                 │                    │                 │
│  8. Extract     │                    │                 │
│     AI Text     │                    │                 │
│                 │                    │                 │
│  9. Display     │                    │                 │
│     to User     │                    │                 │
└─────────────────┘                    └─────────────────┘

Request Headers:
├─ Content-Type: application/json
├─ Accept: application/json
└─ User-Agent: python-requests/[version]

Response Headers:
├─ Content-Type: application/json
├─ Content-Length: [size]
└─ Status: 200 OK (success) or error code
```

## Prompt Engineering Framework

### System vs User Prompt Strategy

```
Prompt Engineering Architecture
┌─────────────────────────────────────────────────────────────────┐
│ System Prompt (AI Personality & Behavior)                      │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ Character Definition                                        │ │
│ │ ├─ "You are Master Oogway..."                              │ │
│ │ ├─ Personality traits and speaking style                   │ │
│ │ └─ Knowledge domain and expertise                          │ │
│ │                                                             │ │
│ │ Response Guidelines                                         │ │
│ │ ├─ Tone and language style                                 │ │
│ │ ├─ Response length and structure                           │ │
│ │ └─ Content appropriateness rules                           │ │
│ │                                                             │ │
│ │ Context and Background                                      │ │
│ │ ├─ Reference materials (Kung Fu Panda)                     │ │
│ │ ├─ Metaphors and wisdom themes                             │ │
│ │ └─ Consistent character voice                              │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│ User Prompt (Specific Question or Task)                        │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ Context Setting                                             │ │
│ │ ├─ "I'm trying to learn Python programming..."             │ │
│ │ ├─ Current situation description                           │ │
│ │ └─ Emotional state (frustrated, excited, etc.)            │ │
│ │                                                             │ │
│ │ Specific Request                                            │ │
│ │ ├─ "What wisdom can you share..."                          │ │
│ │ ├─ Clear question or problem statement                     │ │
│ │ └─ Desired outcome or help needed                          │ │
│ │                                                             │ │
│ │ Connection to Character                                     │ │
│ │ ├─ "Po probably felt the same way..."                      │ │
│ │ ├─ Reference to character's world                          │ │
│ │ └─ Bridge to character's expertise                         │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Learning Progression

This module establishes the foundation for AI integration:

1. **HTTP Communication**: Students learn to make web requests
2. **JSON Data Handling**: Processing structured data exchange
3. **Error Management**: Building resilient network applications
4. **AI Interaction**: Understanding prompts and responses
5. **Service Testing**: Validating external dependencies
6. **User Experience**: Creating engaging AI-powered applications

## Real-World Applications

The skills taught in this module are essential for:

- **Chatbot Development**: Building conversational AI applications
- **Content Generation**: Using AI for writing, translation, summarization
- **Data Analysis**: Leveraging AI for insights and processing
- **Educational Tools**: Creating AI-powered learning experiences
- **Creative Applications**: AI-assisted art, music, and storytelling
- **API Integration**: Working with any external web service

By the end of this module, students understand how to integrate AI services into their applications while building robust error handling to ensure reliable user experiences.