"""based on token_generator_4 but hard-wired to only give donkeys.
gives user feedback on the number of rounds and maintains a balance.
test amount set to 5"""

import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds played
    number = random.randint(6, 36)  # can only be a donkey
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
    if balance >=1:
        play_again = input("press x to quit and any other key to play a second round: ")
    else:
        print("sorry you have run out of money")
        play_again = "x"

print("Thanks for playing!")
print(f"You started with ${TEST_AMOUNT:.2f}, and you leave with ${balance:.2f}")
print("goodbye")
