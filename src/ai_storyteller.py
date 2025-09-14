"""
AI Storyteller Interface - FOR FUTURE SESSIONS (Days 4-5)

INSTRUCTOR NOTES:
This file is a simple stub for Day 1. It provides basic functionality
so the game doesn't crash, but the real AI features will be implemented
in later sessions when students are ready.

Key concepts for later sessions:
1. API communication with Ollama
2. Prompt engineering for kid-friendly content
3. Error handling for network issues
4. Fallback behavior when AI isn't available

For Day 1: Students should know this exists but not worry about it.
"""

import config

class AIStoryteller:
    """
    Handles AI-powered story enhancement
    
    INSTRUCTOR: For Day 1, this is just a placeholder.
    The real implementation will come in Days 4-5 when students
    understand the basics and are ready for advanced features.
    """
    
    def __init__(self):
        """
        Initialize the AI storyteller
        
        For Day 1, we just create a simple stub that's not available.
        This prevents errors without implementing complex AI features.
        """
        
        # For Day 1, AI is not available
        self.available = False
        self.url = config.OLLAMA_URL
        self.model = config.MODEL_NAME
        
        if config.DEBUG_MODE:
            print("🔧 DEBUG: AI Storyteller created (Day 1 stub version)")
            print(f"🔧 DEBUG: AI Available: {self.available}")
    
    def is_available(self) -> bool:
        """
        Check if AI storytelling is available
        
        Returns:
            False for Day 1 (will be implemented properly later)
        """
        return self.available
    
    def enhance_description(self, base_text: str, history: list) -> str:
        """
        Enhance a story description with AI (Day 4-5 feature)
        
        For Day 1, this just returns the original text unchanged.
        Students will implement the real AI enhancement later.
        
        Args:
            base_text: The original story description
            history: List of choices made so far
            
        Returns:
            For Day 1: Just the original text
            For Day 4-5: AI-enhanced description
        """
        
        if config.DEBUG_MODE:
            print("🔧 DEBUG: AI enhancement requested (returning original text for Day 1)")
        
        # Day 1: Just return the original text
        # Day 4-5: Students will implement AI enhancement here
        return base_text
    
    def test_connection(self) -> bool:
        """
        Test if we can connect to the AI service
        
        For Day 1, always returns False.
        For Day 4-5, will test actual connection to Ollama.
        
        Returns:
            False for Day 1 implementation
        """
        
        if config.DEBUG_MODE:
            print("🔧 DEBUG: AI connection test (always False for Day 1)")
        
        return False

"""
INSTRUCTOR NOTES FOR FUTURE SESSIONS:

DAY 4-5 IMPLEMENTATION GOALS:
When students are ready for AI features, this file will be expanded with:

1. REAL CONNECTION TESTING:
   def test_connection(self) -> bool:
       try:
           response = requests.get(f"{self.url}/api/tags", timeout=2)
           return response.status_code == 200
       except:
           return False

2. AI ENHANCEMENT:
   def enhance_description(self, base_text: str, history: list) -> str:
       if not self.available:
           return base_text
       
       prompt = f'''You are a friendly storyteller for kids aged 8-11.
       Enhance this story segment, keeping it short (2-3 sentences), 
       age-appropriate, and exciting.
       
       Story so far: {' '.join(history[-3:])}
       Current scene: {base_text}
       
       Enhanced description:'''
       
       # Make API call to Ollama here
       # Return enhanced text or fallback to original

3. CONTENT FILTERING:
   def filter_content(self, text: str) -> str:
       # Check for inappropriate content
       # Return filtered/safe version

4. PROMPT CUSTOMIZATION:
   Students can modify prompts to change the AI's personality:
   - Funny storyteller
   - Mysterious narrator  
   - Educational guide
   - Different story themes

TEACHING PROGRESSION:
- Day 4: Explain APIs, show simple connection testing
- Day 5: Implement prompt engineering, content filtering
- Advanced: Custom personalities, multiple AI models

SAFETY CONSIDERATIONS:
- Always run locally or on instructor's machine
- Content filtering for age-appropriate responses  
- Fallback to original text if AI fails
- No external API calls or data collection
"""