# Task:
# Refactor your ATM PIN system into modular functions.
# Create separate functions for:
# PIN validation, attempt tracking, user input handling, and main program flow.
# Add a function that generates transaction history logs.

import random
import datetime
from datetime import datetime

# Checks if PIN is 4 digits.
def validate_pin(user):
    return user.isdigit() and len(user) == 4


# Tracks remaining attempts.
def is_locked(attempts):
    return attempts == 0


# Records each attempt to a file.
def log_transaction(date,attempts,success ):
    with open("transaction_history.txt", "a") as file:
        file.write(f"{date} - PIN attempt: {success} - Attempts left: {attempts}\n")



# Runs the program flow.
def main():
    pin = random.randint(0, 9999)
    pin = f"{pin:04d}"
    print(pin)  # Uncomment for testing only

    attempts = 3

    while attempts > 0:
    #Get PIN from user
        user = input("Enter PIN (4-digits)")

        if not validate_pin(user):
            print("Invalid. Please add 4 digits number")
            continue

        attempts -= 1

        if user == pin:
            date = datetime.now()
            log_transaction(date,attempts,success=True)
            print("Welcome")
            break

        elif user != pin:
            date = datetime.now()
            log_transaction(date, attempts,success=False)

    # if attempts reach 0.
        if is_locked(attempts):
            print("The account is LOCKED")
            break
    # else.
        print(f"Invalid\nYou got {attempts} attempts")

    #Emergincy Exit.
        try:
            choice = int(input("Enter an Operator (1/2):\n1.Try again.\n2.Quit.\n>>> "))
        except ValueError:
            print("Enter a valid operator")
            continue

        if choice == 1:
            continue
        elif choice == 2:
            print("Program Exit")
            break
        else:
            print("Invalid Operator")
            continue


main()