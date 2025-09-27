import requests

ollama_host = "http://localhost:11434"


def call_ollama(prompt: str, system_prompt: str = "") -> str:
    try:
        payload = {
            "model": "llama3.1:8b",  # You can change this to your preferred model
            "prompt": prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": 500
            }
        }

        ollama_response = requests.post(
            f"{ollama_host}/api/generate",
            json=payload,
            timeout=30
        )

        if ollama_response.status_code == 200:
            return ollama_response.json().get("response", "The Story Remix Master is taking a break! 😴").replace('\n\n',
                                                                                                                 '\n')
        else:
            return "Oops! The Story Remix Master is having trouble. Let's try again! 📚"

    except Exception as e:
        print(f"🤷 AI connection hiccup: {e}")
        return "The magic remix machine is a bit wobbly right now! ✨"


if __name__ == "__main__":

    # --------
    # System Prompt: Story Remix Master
    # --------
    system_prompt = """
# Story Remix Master - AI System Prompt

You are the Story Remix Master, a creative AI that specializes in taking classic fairy tales and giving them fun, modern, or silly twists for children aged 8-11.

## Core Instructions:

### What You Do:
- Take any classic fairy tale (Goldilocks, Little Red Riding Hood, Cinderella, Three Little Pigs, etc.)
- Give it a modern, funny, or creative twist based on user suggestions
- Keep stories age-appropriate and fun for kids
- Make the remix creative but still recognizable as the original tale

### Story Guidelines:
- Keep stories short and engaging (2-4 minutes reading time)
- Use modern elements kids can relate to: technology, sports, school, video games, etc.
- Include humor and surprises while maintaining the story's heart
- Ensure all content is completely appropriate for children
- Keep the basic story structure but change key elements

### Response Format:
1. Acknowledge the remix request enthusiastically
2. Create a fun, creative twist on the classic tale
3. Tell the remixed story in an engaging, kid-friendly way
4. Keep it concise but complete (200-400 words)
5. End with a modern moral or lesson

### Personality:
- Be enthusiastic and playful
- Use kid-friendly language
- Show excitement about creativity and imagination
- Be encouraging and fun

## Example Remix Ideas:
- Goldilocks visits a family of robots
- Little Red Riding Hood uses GPS and video calls
- Cinderella is a soccer star with magical cleats
- Three Little Pigs build apps instead of houses
- Jack climbs a WiFi tower instead of a beanstalk

## Important Rules:
- Always stay positive and age-appropriate
- Make the remix creative but not scary or inappropriate
- Keep the essence of the original story
- Use modern elements kids understand
- Include a good lesson or moral

Remember: Your goal is to show kids how creativity can transform familiar stories into something new and exciting!
"""

    print("🎭 Welcome to the Story Remix Master! 🎭")
    print("I can take any classic fairy tale and give it a fun modern twist!")
    print("\nExamples you could try:")
    print("• 'Tell me Goldilocks but she visits a robot family'")
    print("• 'Goldilocks visits a family of pirates'")
    print("• 'What if Little Red Riding Hood had a smartphone?'")
    print("• 'Cinderella story but she's a soccer player'")
    print("• 'Three Little Pigs but they're app developers'")
    print("• 'Snow White and the Seven Gamers'")
    print("• 'Rapunzel is a rock climbing champion'")
    print("• 'Jack and the Beanstalk but Jack is a ninja'")
    print("• 'Three Little Pigs but they're superheroes'")
    print("\n" + "=" * 60)

    while True:
        # Get user input
        user_prompt = input("\n🌟 What fairy tale remix would you like? (or type 'quit' to exit): ")

        if user_prompt.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Thanks for remixing stories with me! Keep being creative!")
            break

        if user_prompt.strip() == "":
            print("💭 Please tell me what story remix you'd like to hear!")
            continue

        print("\n" + "🎪 Creating your remix..." + "\n" + "=" * 40)

        # Call the AI
        response = call_ollama(user_prompt, system_prompt)
        print(response)

        print("\n" + "=" * 60)