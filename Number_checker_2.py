"""number checker script for lucky unicorn version 2"""

error = "<syntax error> please enter a whole number between 1 and 10\n"
valid = False

while not valid:
    try:
        user_balance = int(input("How much money do you want to play with?: "))

        # check for valid numbers
        if 1 <= user_balance <= 10:
            user_balance = int(input("Please enter a whole number between 1 and 10"))
            print(f"you are playing with ${user_balance}")
            valid = True
        else:
            print(error)
    except ValueError:
        print(error)
