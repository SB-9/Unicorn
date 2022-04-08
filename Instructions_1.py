"""Instructions script for lucky unicorn version 1"""


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
    print("program continues")
    print()


played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()
