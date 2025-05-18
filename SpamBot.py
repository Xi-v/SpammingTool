import keyboard as k
import time

def discord():
    discord_method = int(input("1. Spam ping\n2. Spam text\n3. Spam ping and text\n4. Back to menu\nEnter a number: "))
    discord_loop = True
    while (discord_loop):
        try:
            if discord_method == 1:
                user = input("Enter user to ping (Enter 'exit' to head back to menu): ")
                if user == 'exit':
                    main()
                    discord_loop = False

                print("You have 3 seconds to switch to the place you want to spam")
                time.sleep(3)
                while True:
                    k.press_and_release("shift+2")
                    time.sleep(0.1)
                    k.write(user)
                    k.press_and_release("enter")
                    time.sleep(0.1)
            
            elif discord_method == 2:
                phrase = input("Enter a phrase to spam (Enter 'exit' to head back to menu): ")
                if phrase == 'exit':
                    main()
                    discord_loop = False

                print("You have 3 seconds to switch to the place you want to spam")
                time.sleep(3)
                while True:
                    k.write(phrase)
                    time.sleep(0.1)
            
            elif discord_method == 3:
                user = input("Enter user to ping (Enter 'exit' to head back to menu): ")
                if user == 'exit':
                    main()
                    discord_loop = False

                phrase = input("Enter a phrase to spam (Enter 'exit' to head back to menu): ")
                if phrase == "exit":
                    main()
                    discord_loop = False

                while True:
                    k.press_and_release("shift+2")
                    time.sleep(0.1)
                    k.write(user)
                    k.press_and_release("enter")
                    time.sleep(0.1)
                    k.press_and_release("space")
                    k.write(phrase)
                    time.sleep(0.1)
            
            elif discord_method == 4:
                main()
                discord_loop = False

        except ValueError:
            print("Invalid, pick a choice")

def other():
    phrase = input("Enter a phrase to spam (Enter 'exit' to head back to menu): ")
    if phrase == "exit":
        main()
    else:
        print("You have 3 seconds to switch to the place you want to spam")
        time.sleep(3)
        while True:
            k.write(phrase)
            time.sleep(0.1)

def main():
    print("How would you like to spam")
    loop = True
    while (loop):
        try:
            method = int(input("1. Discord Spam\n2. Other\nEnter a number: "))
            if method == 1:
                discord()
                loop = False
            elif method == 2:
                other()
                loop = False
            else:
                print("Choose an option")
        except ValueError:
            print("Error, enter a number.")

main()