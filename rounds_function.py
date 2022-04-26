"""rounds version 3, turned into a function"""

import random


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


# main routine
starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing!")
print(f"You started with ${starting_balance:.2f}, and you leave with ${closing_balance:.2f}")
print("goodbye")
