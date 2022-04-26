"""base component for lucky unicorn"""

import random


# yes no checker function
def yes_no(question):
    # ask if user has played the game before
    answer = input(question)

    # check for unexpected inputs
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("<syntax error> Please enter y or n: ")

    # check for yes
    if answer.lower() == "y":
        return "Yes"

    # others=wise show instructions
    else:
        return "No"


# instructions function
def instructions():
    print("How to play the game")
    print()
    print("instructions go here")
    print()


# number checker function
def num_check(question, low, high):
    error = "<syntax error> that was not a valid input\n" \
            "Please enter a number between {} and {}".format(low, high)

    # keep asking until a valid input is entered
    while True:
        try:
            # ask for a number
            response = int(input(question))

            # check the number is in required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# function to generate a random token
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds played
        number = random.randint(1, 100)  # can only be a donkey
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
        # else if randint rolls 6 to 36 select donkey and adjust balance
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
        # else if randint rolls an even number select zebra and adjust balance
        elif number % 2 == 0:
            token = "zebra"
            balance -= .50
        # else select horse and adjust balance
        else:
            token = "horse"
            balance -= .50
        print(f"Token: {token}, Balance = ${balance:.2f}, rounds played = {rounds_played}")
        if balance >= 1:
            play_again = input("press x to quit and any other key to play a second round: ")
        else:
            print("sorry you have run out of money")
            play_again = "x"
    return balance


played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()
# ask how much money the user wants to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"You started with ${starting_balance:.2f}, and you leave with ${closing_balance:.2f}")
print("goodbye")
