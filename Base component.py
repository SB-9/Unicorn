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
    print()
    print(formatter("How to play", "*"))
    print()
    print("Choose a starting amount to play with - it needs to be an integer between 1 and 10")
    print()
    print("then press <enter> to play")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back. These are the payout amounts:\n"
          "\t Unicorn: $5.00 (balance increases by $4.00)\n"
          "\t Horse: $0.50 (balance decreases by $0.50)\n"
          "\t Zebra: $0.50 (balance decreases by $0.50)\n"
          "\t Donkey $0.00 (balance decreases by $1.00)\n")
    print("\n See if you can avoid Donkeys, Get unicorns, and finish with "
          "more money than you started with.\n")
    print("*" * 50)
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

    while play_again != "x":
        rounds_played += 1  # keep track of rounds played
        number = random.randint(1, 100)  # can only be a donkey
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4
            print(formatter("Congratulations, you got a Unicorn", "!"))
            print()
        # else if randint rolls 6 to 36 select donkey and adjust balance
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1
            print(formatter("Bad luck, you got a Donkey", "D"))
            print()
        # else if randint rolls an even number select zebra and adjust balance
        elif number % 2 == 0:
            token = "zebra"
            balance -= .50
            print(formatter("You got a Zebra", "Z"))
            print()
        # else select horse and adjust balance
        else:
            token = "horse"
            balance -= .50
            print(formatter("You got a Horse", "H"))
            print()
        print(f"Token: {token}, Balance = ${balance:.2f}, rounds played = {rounds_played}")
        print()
        if balance >= 1:
            play_again = input("press x to quit and any other key to play a second round: ")
        else:
            print("sorry you have run out of money")
            play_again = "x"
    return balance


# function to format the text output
def formatter(text, symbol):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("Welcome to the Unicorn Game", "-"))
print()

played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()
# ask how much money the user wants to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"You started with ${starting_balance:.2f}, and you leave with ${closing_balance:.2f}")
print(formatter("Goodbye", "*"))
