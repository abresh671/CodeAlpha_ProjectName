def simple_chatbot():
    """
    A simple rule-based chatbot that responds to predefined inputs.
    """
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "hey":
            print("Chatbot: hey there!")    
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop
        else:
            print("Chatbot: I don't understand that. Can you try 'hey', 'hello', 'how are you', or 'bye'?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()