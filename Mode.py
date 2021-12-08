#!usr/bin/env python3


print("Hey man! What's your name?")

name = input()

print("Hello " + str(name) + "! My name is Python...Wanna play a game?")

choice = input()

if choice == "yes":
    print("Yaay! Alright, let us start, shall we? Please type any word that you can think of and hit ENTER...")
    word = input()
    print("Great! Choose a mode for your word and watch me do magic!: \n1. Upper Case\n2. Lower Case")
    mode = input()

    if mode == "1":
        print("Your word is: " + str(word.upper()))
    elif mode == "2":
        print("Your word is: " + str(word.lower()))

elif choice == "no":
    print("No worries...Have a good day!")
