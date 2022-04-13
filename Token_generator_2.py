"""token generator script for lucky unicorn version 2"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100

# testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # can wrap output making it easier to screenshot

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

print(balance)
