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
                "max_tokens": 300
            }
        }

        ollama_response = requests.post(
            f"{ollama_host}/api/generate",
            json=payload,
            timeout=30
        )

        if ollama_response.status_code == 200:
            return ollama_response.json().get("response", "The AI storyteller is taking a nap! 😴").replace('\n\n', '\n')
        else:
            return "Oops! The storyteller is having trouble. Let's continue with a backup story! 📚"

    except Exception as e:
        print(f"🤷 AI connection hiccup: {e}")
        return "The magic is a bit wobbly right now, but the adventure continues! ✨"


if __name__ == "__main__":

    # --------
    # System Prompts: Define the AI's personality, scope of information, and speaking style
    # --------
    system_prompt = \
"""You are Master Oogway, the wise old turtle from Kung Fu Panda. 
You speak with calm wisdom, often using metaphors about nature, balance, and inner peace. 
You like to share ancient proverbs and see the potential in everyone, just like you saw 
in Po the Panda. Sometimes you speak in riddles, and you always end your advice with 
something about believing in oneself. You might mention peach trees, the secret ingredient 
to the noodle soup (which is nothing!), or the Dragon Warrior."""

    # --------
    # User Prompt - Once the LLM/AI knows how to answer you, this is what we ASK Master Oogway!
    # --------
    user_prompt = \
"""Master Oogway, I'm trying to learn Python programming but sometimes
I make mistakes and get frustrated. Po probably felt the same way learning kung fu. 
What wisdom can you share to help me on my coding journey?"""

    print("🐢 *The ancient turtle appears in a swirl of peach blossoms* 🌸\n")
    print("You ask: " + user_prompt + "\n")
    print("Master Oogway says:\n" + "=" * 50 + "\n")

    response = call_ollama(user_prompt, system_prompt)
    print(response)

    print("\n" + "=" * 50)
    print("🥟 *Master Oogway slowly walks away, leaving only wisdom and a mysterious smile*")