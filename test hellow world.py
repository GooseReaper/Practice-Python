
from random import choice, random

import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # just to resolve local IP
        return s.getsockname()[0]
    finally:
        s.close()


def hellow_world_game():
    print("select one the option below: \n 1. array print letter by letter \n 2. print entire string \n 3. Print Letter[i] \n 4. exit")
    hello_world = "Hello, World!"
    arr = len(hello_world)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        for i in range(arr):
            print(hello_world[i])
    elif user_input == "2":
        print(hello_world)
    elif user_input == "3":
        print("max bounds: 0 to", arr - 1)
        i = int(input("Enter the index of the letter you want to print: "))
        if 0 <= i < arr:
            print(hello_world[i])
        else:
            print("Index out of bounds.")
    elif user_input == "4":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")

    print("Do you want to continue? (y/n): ")
    user_input = input().lower()
    if user_input == "y":
        print("Continuing...")
        hellow_world_game()
    elif user_input == "n":
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
def risky():
    print("This is a risky game...")
    print("Do You Want To Play? (y/n): ")
    user_input = input().lower()
    if user_input == "y":
        print("Playing...")
        
    else:
        print("Exiting...")
        return
    print("Guess a letter from the alphabet: ")
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_awnser = choice(letter)
    letter_input = input().lower()
    if letter_input == letter_awnser:
        print("Correct!")
        print("You guessed it right!")
        print("Take Care!")
    else:
        print("Incorrect.")
        print("The correct letter was:", letter_awnser)
        print("So sorry!")
        ip = get_local_ip()
        print("Local IP Address:", ip)
        print("See You Soon....")
hellow_world_game()
risky()
