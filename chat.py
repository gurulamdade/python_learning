import datetime

chat_history = []

def login():
    print("------ LOGIN SYSTEM ------")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login Successful!\n")
        menu()
    else:
        print("Invalid Login\n")
        login()


def menu():
    while True:
        print("\n------ MAIN MENU ------")
        print("1. Start Chat")
        print("2. View Chat History")
        print("3. Help")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            chat()
        elif choice == "2":
            show_history()
        elif choice == "3":
            help_menu()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice")


def chat():
    print("\n------ CHAT SYSTEM ------")
    print("Type 'bye' to stop chatting")

    while True:
        user = input("You: ").lower()
        chat_history.append("You: " + user)

        if user == "hello":
            reply = "Hello! Nice to meet you."
        elif user == "hi":
            reply = "Hi there!"
        elif user == "how are you":
            reply = "I am fine. Thanks for asking."
        elif user == "what is your name":
            reply = "I am Python Chat Bot."
        elif user == "who created you":
            reply = "guru lamdade."
        elif user == "time":
            reply = str(datetime.datetime.now().time())
        elif user == "date":
            reply = str(datetime.date.today())
        elif user == "help":
            reply = "You can ask about time, date, or basic questions."
        elif user == "bye":
            reply = "Goodbye!"
            print("Bot:", reply)
            chat_history.append("Bot: " + reply)
            break
        else:
            reply = "Sorry, I don't understand."

        print("Bot:", reply)
        chat_history.append("Bot: " + reply)


def show_history():
    print("\n------ CHAT HISTORY ------")

    if len(chat_history) == 0:
        print("No chat history found.")
    else:
        for msg in chat_history:
            print(msg)


def help_menu():
    print("\n------ HELP ------")
    print("Commands you can use:")
    print("hello")
    print("hi")
    print("how are you")
    print("what is your name")
    print("time")
    print("date")
    print("bye")


login()