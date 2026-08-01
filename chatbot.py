import json

# ANSI Escape Codes for UI Colors
BOT_COLOR = '\033[94m'  # Blue
USER_COLOR = '\033[92m' # Green
RESET_COLOR = '\033[0m' # Reset text back to normal

def load_knowledge_base(filepath):
    """Loads the external dictionary database."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{BOT_COLOR}Bot: Error - Knowledge base file not found!{RESET_COLOR}")
        return {}

def main():
    print(f"{BOT_COLOR}Bot: Hello!, How can i help you? Type 'exit' to quit.{RESET_COLOR}")
    
    # Load the JSON data once at startup
    responses = load_knowledge_base('intents.json')

    # The Infinite Cycle
    while True:
        # Phase 1: Input & Sanitization
        raw_input = input(f"{USER_COLOR}You: {RESET_COLOR}")
        clean_input = raw_input.lower().strip()

        # Phase 2: Exit Strategy
        if clean_input == 'exit':
            print(f"{BOT_COLOR}Bot: Powering down. It was great chatting with you!{RESET_COLOR}")
            break

        # Phase 3: Nested Conditions (Dynamic Branch)
        if 'robotics' in clean_input:
            print(f"{BOT_COLOR}Bot: Robotics is amazing! Are you working on autonomous controllers or hardware?{RESET_COLOR}")
            follow_up = input(f"{USER_COLOR}You: {RESET_COLOR}").lower().strip()
            
            if 'autonomous' in follow_up or 'controller' in follow_up:
                print(f"{BOT_COLOR}Bot: Awesome! Python is incredible for spatial navigation.{RESET_COLOR}")
            elif 'hardware' in follow_up or 'circuit' in follow_up:
                print(f"{BOT_COLOR}Bot: Very cool. Building physical logic circuits takes serious skill!{RESET_COLOR}")
            else:
                print(f"{BOT_COLOR}Bot: That sounds like a brilliant project! I'm cheering you on.{RESET_COLOR}")
            continue
        
        # Phase 4: Intelligent Intent Matching (Substring Search)
        reply = "I am not quite sure I understand, but I am always happy to learn!"
        for intent, response in responses.items():
            if intent in clean_input:  # Scans the whole sentence for the keyword
                reply = response
                break

        print(f"{BOT_COLOR}Bot: {reply}{RESET_COLOR}")

if __name__ == "__main__":
    main()