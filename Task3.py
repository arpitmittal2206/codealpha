# TASK 3 : BASIC CHATBOT...

def chatbot():
    print("Welcome! I am a simple chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm here to assist you!")
        elif "name" in user_input:
            print("Chatbot: My name is Chatbot.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot()
