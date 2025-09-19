import requests
import configparser

def call_ollama(ollama_host: str, prompt: str, system_prompt: str = "") -> tuple[bool, str]:
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
            response_text = ollama_response.json().get("response", "")
            if response_text:
                return True, response_text.replace('\n\n', '\n')
            else:
                return False, "Empty response from Ollama"
        else:
            return False, f"HTTP {ollama_response.status_code}: {ollama_response.text}"

    except requests.exceptions.Timeout:
        return False, "Request timed out"
    except requests.exceptions.ConnectionError:
        return False, "Connection error - Ollama may not be running"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def get_story_content(current_story: dict, story_graph: dict, ollama_host: str, ) -> str | None:
    title = current_story["title"]
    connections = current_story["connections"]

    # Get available choice titles of the current story, because the story id is not good to describe the next location
    available_choices = []
    for next_story_id in connections:
        available_choices.append(story_graph[next_story_id]['title'])

    system_prompt = \
"""
You are a friendly storyteller for children aged 8-11.

Create fun, safe, magical adventures. Use simple words, be encouraging, and always keep stories appropriate for kids. Include light humor and wonder.

Stories should be 3-4 sentences long and end with excitement about the choices ahead.
 
You will be asked to incorporate ending instructions provided between <ending_instruction> tags and optional choices between <choices_text> tags. 

If no choices are provided between the tag, the story has ended.

IMPORTANT:
---------- 
* Write in SECOND PERSON using 'you' - make the reader the hero of the story.
    * Example: "You step into the magical forest and feel..."
    * Do NOT write: "Lily steps into the forest..." or "A girl named..." 
* Do not use third person or character names like 'Lily'. The reader IS the adventurer.
* If next locations are provided, you MUST reference them by their EXACT names.
* Do not make up different location names. Use only the provided location titles.
* Never label options with any markers (e.g., A), 1., •, -, etc.) - present all options without labels, numbers, letters, or bullets.

Choice Options - NEGATIVE EXAMPLE:
----------
If the choices where 🌊 Sparkling Pool,🌋 The Rumbling Volcano Pass, then the following examples would be invalid:

<example>
A) Dive into the pool and become a brilliant rainbow-colored adventurer!
B) Follow the sparkling reflections to see what kind of wonders they lead you to!
</example>

Choice Options - POSITIVE EXAMPLE:
----------
If the choices where 🌊 Sparkling Pool,🌋 The Rumbling Volcano Pass, then the following examples would be valid:

<example>
Please chose to either dive into the sparkling pool and become a brilliant rainbow-colored adventurer or follow the path down the pass that looks to lead to a volcano.
</example>

Locations - NEGATIVE EXAMPLE:
----------
Do not include the tags <locations> in your response.

<example>
Please choose to either visit <locations>🏠 The Cozy Tree House</locations>, where the tree's whispers have mentioned a warm and inviting home filled with books and cozy nooks, or head into <locations> 🕳️ The Glowing Underground Cave</locations>, where strange bioluminescent creatures are said to light up the darkness.
</example>

locations - POSITIVE EXAMPLE:
----------

Do not include the tags <locations> in your response.

<example>
Please choose to either visit 🏠 The Cozy Tree House, where the tree's whispers have mentioned a warm and inviting home filled with books and cozy nooks, or head into 🕳️ The Glowing Underground Cave, where strange bioluminescent creatures are said to light up the darkness.
</example>

"""

    # Build the prompt with available choices
    choices_text = ""
    if available_choices:
        choices_text = f"\nThe next available locations are:\n<locations>{', '.join(available_choices)}</locations>"
        ending_instruction = "\nEnd by asking the reader to choose between these specific locations."
    else:
        ending_instruction = "\nEnd with anticipation for what happens next."

    # Clear, simple prompt for Ollama
    user_prompt = \
        f"""
Tell a short, exciting story about: {title}

Write in SECOND PERSON using 'you' - the reader is the hero.
The story should be magical and fun for kids.
Make it 2-3 sentences.
Include wonder and adventure.
{ending_instruction}
{choices_text}

"""
    success, response = call_ollama(ollama_host, user_prompt, system_prompt)
    if success:
        return response
    else:
        print('Unable to talk to Ollama.')
        return None

def load_graph_from_ini(filename='data.ini') -> dict:
    config = configparser.ConfigParser()
    config.read(filename)

    data = {}

    for section in config.sections():
        single_node_data = {
            'title': config.get(section, 'title'),
            'requires_items': [item.strip() for item in config.get(section, 'requires_items').split(',') if item.strip()],
            'connections': [conn.strip() for conn in config.get(section, 'connections').split(',') if conn.strip()],
            'item_reward': config.get(section, 'item_reward') if config.get(section, 'item_reward') != 'None' else None
        }
        data[section] = single_node_data

    return data


def save_to_ini(story_id, story, filename='stories.ini'):
    config = configparser.ConfigParser()

    # Read existing INI file if it exists to append new sections
    try:
        config.read(filename)
    except Exception as e:
        print(f"Error reading INI file: {e}")

    # Add the story under a section named after the story_id
    config[story_id] = {
        'story': story
    }

    # Write to the INI file
    try:
        with open(filename, 'w') as configfile:
            config.write(configfile)
        print(f"Story saved to {filename} under section [{story_id}]")
    except Exception as e:
        print(f"Error writing to INI file: {e}")


if __name__ == "__main__":

    ollama_host = "http://localhost:11434"

    graph = load_graph_from_ini()

    for node_id, node_data in graph.items():
        story = get_story_content( current_story=node_data, story_graph=graph, ollama_host=ollama_host )

        save_to_ini( story_id=node_id, story=story )