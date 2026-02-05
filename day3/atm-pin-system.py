# Task:
# Build a secure PIN entry system for a bank ATM.
# The user has 3 attempts to enter the correct 4-digit PIN (1234)
# After 3 wrong attempts, lock the account. Include an emergency cancel option.

import random


pin = random.randint(0,9999)
pin = int(f"{pin:04d}")
#print(pin)               # Uncomment for testing only
attempts = 3

while attempts > 0:

    try:
        user = int(input("Enter PIN (4-digits)"))
    except ValueError:
        print("Add a valid PIN")
        continue

    attempts -= 1

    if user == pin:
        print("Welcome")
        break

    elif user != pin:
        if attempts == 0:
            print("The account is LOCKED")
            break
        print(f"Invalid\nYou got {attempts} attempts")

        try:
            choice = int(input("Enter an Operator (1/2):\n1.Try again.\n2.Quit.\n>>> "))
        except ValueError:
            print("Enter a valid operator")

        if choice == 1:
            continue
        elif choice == 2:
            print("Program Exit")
            break
        else:
            print("Invalid Operator")
            continue