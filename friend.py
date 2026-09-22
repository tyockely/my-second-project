import time

while True:
    print("Do you want to be my friend?")
    time.sleep(1)

    choice = input(
        "1. Yes I want to be your friend. 2. No I don't want to be your friend. ")

    if choice == "2":
        print("I don't want to be your friend either.")
        time.sleep(3)
        print("Why though?")

        user_input = input(
            "1. I don't like you. 2. I don't like your personality. 3. I don't like your face. ")

        if user_input == "1":
            print("That's not very nice.")
            time.sleep(3)
            print("I don't like you either.")
            break
        elif user_input == "2":
            print("That's not very nice.")
            time.sleep(3)
            print("I don't like your personality either.")
            break
        elif user_input == "3":
            print("That's not very nice.")
            time.sleep(3)
            print("I don't like your face either.")
            break
        break
    elif choice == "1":
        print("Yay! I'm glad you want to be my friend.")
        time.sleep(3)
        print("I like you too!")
        time.sleep(1)
        print("What is your name? Type your name here: ")
        user_name = input()
        print("Nice to meet you, " + user_name + "!")
        break
    else:
        print("Choose a real choice")