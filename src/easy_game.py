"""
SUPER SIMPLE Choose Your Own Adventure Game
Now with easy-to-edit story file!
"""

def load_story():
    """Load story from the simple text file"""
    story = {}
    current_section = None
    
    with open("../story.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            # If line has no spaces, it's a section name
            if " " not in line and "->" not in line:
                current_section = line
                story[current_section] = {"text": "", "choices": []}
            # If line has ->, it's a choice
            elif "->" in line:
                choice_text, next_section = line.split(" -> ")
                story[current_section]["choices"].append({
                    "text": choice_text,
                    "next": next_section
                })
            # Otherwise, it's story text
            else:
                if story[current_section]["text"]:
                    story[current_section]["text"] += "\n"
                story[current_section]["text"] += line
    
    return story

def play_section(story, section_name):
    """Play one section of the story"""
    section = story[section_name]
    
    print("\n" + "="*50)
    print(section["text"])
    
    # If no choices, game ends
    if not section["choices"]:
        return None
    
    # Show choices
    print("\nWhat do you want to do?")
    for i, choice in enumerate(section["choices"], 1):
        print(f"{i}. {choice['text']}")
    
    # Get player choice
    while True:
        try:
            choice_num = int(input(f"\nPick a number (1-{len(section['choices'])}): "))
            if 1 <= choice_num <= len(section["choices"]):
                return section["choices"][choice_num - 1]["next"]
            else:
                print("Invalid choice! Try again.")
        except ValueError:
            print("Please enter a number!")

def main():
    """Main game function"""
    story = load_story()
    current_section = "START"
    
    while current_section:
        current_section = play_section(story, current_section)

if __name__ == "__main__":
    main()