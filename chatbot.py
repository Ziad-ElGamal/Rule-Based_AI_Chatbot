# The Knowledge Base (Expanded Vocab & Friendly Personality)
responses = {
    'hello': 'Hey there! It is so great to meet you. How can I help you today?',
    'how are you':' I am doing fantastic! Thanks for asking. How about you?',
    'bye': 'Goodbye! Have an absolutely wonderful day!',
    'status': 'All systems are humming along perfectly! We are good to go.',
    'mission': 'My mission is to be your friendly assistant and help you crush Project 1!',
    'joke': 'Why do programmers prefer dark mode? Because light attracts bugs! Haha!',
    'python': 'Python is fantastic! It is my favorite tool for data extraction and automation scripts.',
    'c++': 'Ah, C++! An absolute powerhouse for competitive programming and high-performance algorithms.',
    'help': 'I would love to help! You can say hello, ask about my status, or let us chat about code.'
}

# The Infinite Cycle
while True:
    # Phase 1: Input & Normalization
    raw_input = input('You: ')
    clean_input = raw_input.lower().strip()

    # Phase 2: Exit Strategy
    if clean_input == 'exit':
        print("Bot: Powering down. It was so great chatting with you! Catch you later.")
        break

    # Phase 3: Nested Conditions (Dynamic Conversation Branch)
    if clean_input == 'robotics':
        print("Bot: Robotics is amazing! Are you working on autonomous controllers or physical hardware today?")
        
        # Waiting for the user's second input
        follow_up = input('You: ').lower().strip()
        
        # The Nested Logic
        if 'autonomous' in follow_up or 'controller' in follow_up:
            print("Bot: Awesome! Python is incredible for things like spatial navigation and sensor logic.")
        elif 'hardware' in follow_up or 'circuit' in follow_up:
            print("Bot: Very cool. Building real physical logic circuit boards takes serious skill!")
        else:
            print("Bot: That sounds like a brilliant project! I'm cheering you on.")
            
        # The 'continue' keyword skips the dictionary lookup below and restarts the main loop
        continue 

    # Phase 4: Intent Matching & Output
    # The fallback response is also updated to be much friendlier!
    reply = responses.get(clean_input, 'I am not quite sure I understand, but I am always happy to learn!')
    print("Bot:", reply)