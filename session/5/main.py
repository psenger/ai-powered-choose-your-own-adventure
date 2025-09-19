#!/usr/bin/env python3
"""
🌟 AI-Powered Choose Your Own Adventure Game 🌟
A magical story adventure for young explorers aged 8-11!

Your mission: Find the three magical crystals to save the Enchanted Forest!
Collect items, make choices, and discover interconnected stories.
"""
import requests
import configparser
from typing import List, Optional


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

def get_story_content(current_story: dict, story_graph: dict, ollama_host: str, stories: dict) -> str:
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
        return stories[current_story["story_key"]]["story"]

def get_available_paths(current_story: dict, story_graph: dict, inventory: set[str]) -> List[str]:

    connections = current_story["connections"]
    available = []

    for story_id in connections:
        required_items = set(story_graph[story_id]['requires_items'])

        # Check if we have all required items
        if required_items.issubset(inventory):
            available.append(story_id)
        else:
            missing_items = required_items - inventory
            print(f"🔒 {story_graph[story_id]['title']} is locked! You need: {', '.join(missing_items)}")

    return available

def print_inventory(inventory: set[str]):
    if len(inventory) == 0:
        print("You don't have any items in your inventory!")
    else:
        print(f"In your inventory you have: {', '.join(inventory)}")


def get_user_choice(options: List[str], story_graph: dict, inventory: set[str]) -> Optional[str]:
    # Check if player has reached a dead end (no available options)
    if not options:
        print("\n" + "=" * 50)
        print("🔚 OH NO! You've reached a DEAD END!")
        print("=" * 50)
        print("\n😔 Your adventure has come to an unexpected halt.")
        print("You look around but there are no paths forward from here.")
        print("\nSometimes adventures end in mysterious ways...")
        print("But every ending is a chance to start a new journey! 🌟")
        print("\n" + "-" * 50)

        while True:
            choice = input("\nYour options: 'i' for inventory, or 'e' to exit: ").strip().lower()

            if choice == 'e':
                print("\n👋 Thank you for playing! Every hero's journey teaches us something new!")
                print("🎮 Try again to discover new paths and unlock different endings!")
                return None
            elif choice == 'i':
                print_inventory(inventory)
            else:
                print("Please enter 'i' for inventory or 'e' to exit.")

    # Normal case - player has available paths
    else:
        while True:
            print("\n🌟 Where would you like to go next?")
            print("-" * 30)

            for i, story_id in enumerate(options, 1):
                title = story_graph[story_id]["title"]
                print(f"{i}. {title}")

            choice = input(f"\nYour choice (1-{len(options)}, 'i' for inventory, or 'e' for exit): ").strip().lower()

            if choice == 'e':
                print("\n👋 Leaving so soon? The forest will await your return!")
                return None

            try:
                if choice == 'i':
                    print_inventory(inventory)
                else:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(options):
                        return options[choice_num - 1]
                    else:
                        print(f"⚠️ Please choose a number between 1 and {len(options)}!")
            except ValueError:
                print("⚠️ Please enter a valid number, 'i' for inventory, or 'e' to exit!")

def load_graph_from_ini(filename='data.ini') -> dict:

    config = configparser.ConfigParser()
    config.read(filename)
    data = {}

    for section in config.sections():
        single_node_data = {
            'story_key': section,
            'title': config.get(section, 'title'),
            'requires_items': [item.strip() for item in config.get(section, 'requires_items').split(',') if item.strip()],
            'connections': [conn.strip() for conn in config.get(section, 'connections').split(',') if conn.strip()],
            'item_reward': config.get(section, 'item_reward') if config.get(section, 'item_reward') != 'None' else None,
        }
        data[section] = single_node_data

    return data

def load_stories_from_ini(filename='stories.ini') -> dict:

    config = configparser.ConfigParser()
    config.read(filename)
    data = {}

    for section in config.sections():
        single_node_data = {
            'story': config.get(section, 'story')
        }
        data[section] = single_node_data

    return data

def collect_rewards(current_story: dict, inventory: set[str]) -> set[str]:
    rewards = current_story.get("item_reward")
    new_inventory = set(inventory)

    if not rewards:
        return new_inventory

    if isinstance(rewards, (list, tuple, set)):
        items = [str(r) for r in rewards]
    else:
        items = [str(rewards)]

    print(f"\n🎁 You found: {', '.join(items)}")
    new_inventory.update(items)
    return new_inventory


def main():
    
    inventory = set()
    current_story_id = "start"

    ollama_host = "http://localhost:11434"
    story_graph = {}
    stories = {}

    try:

        print("🧙‍♂️ CHOOSE YOUR OWN ADVENTURE 🧙‍♀️")
        # print("\n🎯 YOUR QUEST: Find the 3 magical crystals to save the Enchanted Forest!")
        print("💡 TIP: Collect special items to unlock secret areas!")
        print("🚪 Remember: You can type 'exit' anytime to end your adventure.\n")
        input("🎮 Press Enter when you're ready to begin your magical journey! ✨")

        story_graph = load_graph_from_ini()
        stories = load_stories_from_ini()

        current_story = story_graph[current_story_id]

        while True:
            story = get_story_content(current_story, story_graph, ollama_host, stories)

            print(story)

            inventory = collect_rewards( current_story, inventory )

            options = get_available_paths( inventory = inventory,
                                           story_graph = story_graph,
                                           current_story = current_story )

            current_story_id = get_user_choice( inventory = inventory, options = options, story_graph = story_graph )

            # Check if user chose to exit
            if current_story_id is None:
                break

            current_story = story_graph[current_story_id]

            if current_story_id == "victory":
                break

    except KeyboardInterrupt:
        print("\n\n👋 Adventure interrupted! The magic will wait for your return! ✨")
    except Exception as e:
        print(f"\n🤖 Oops! Something magical happened: {e}")
        print("🔧 Don't worry - adventures sometimes have unexpected twists!")


if __name__ == "__main__":
    main()
