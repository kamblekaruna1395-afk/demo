print("Chatbot: Hi! I am a simple bot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hello there!")

    elif user == "hi":
        print("Chatbot: Hi! How can I help you?")

    elif user == "how are you":
        print("Chatbot: I'm fine, thanks! What about you?")

    elif user == "what is your name":
        print("Chatbot: I'm a Python chatbot.")

    elif user == "what can you do":
        print("Chatbot: I can answer simple questions using if-else logic.")

    elif user == "how is the weather":
        print("Chatbot: It's sunny today ")

    elif user == "what is python":
        print("Chatbot: Python is a popular programming language.")

    elif user == "who created you":
        print("Chatbot: I was created using Python code by a developer.")

    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "tell me a joke":
        print("Chatbot: Why did the computer go to the doctor? Because it had a virus 😂")

    elif user == "what is 2+2":
        print("Chatbot: 2 + 2 = 4")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day ")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")