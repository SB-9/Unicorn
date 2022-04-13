"""token generator script for lucky unicorn version 3 70% chance of horse or zebra, 20% chance of donkey and 10% chance of unicorn"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra", "horse", "horse", "horse", "zebra", "zebra", "donkey",]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loops until 100 tokens
for item in range(1000):
    token = random.choice(tokens)

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 2
    else:
        balance -= .50

print(f"starting balance = ${STARTING_BALANCE:.2f}")
print(f"final balance = ${balance:.2f}")
