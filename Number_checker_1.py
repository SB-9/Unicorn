"""number checker script for lucky unicorn version 1"""

# Ask the user how much money they want to play with
user_balance = int(input("How much money do you want to play with?: "))

# check for valid numbers
while not 1 <= user_balance <= 10:
    user_balance = int(input("Please enter a whole number between 1 and 10"))

print(f"you are playing with ${user_balance}")
