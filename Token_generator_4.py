"""token generator script for lucky unicorn version 4 65% chance of horse or zebra, 30% chance of donkey and 5% chance of unicorn"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# adjust balance
for item in range(10):
    number = random.randint(1, 100)
    # if the randint rolls 1 to 5 select unicorn and adjust balance
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
    print(f"Token: {token}, Balance = ${balance:.2f}")
print(f"starting balance = ${STARTING_BALANCE:.2f}")
print(f"final balance = ${balance:.2f}")

