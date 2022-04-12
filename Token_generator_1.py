"""token generator script for lucky unicorn version 1"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]

# testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # can wrap output making it easier to screenshot
