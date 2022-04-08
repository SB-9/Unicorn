"""base component for lucky unicorn"""


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


played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()
# ask how much money the user wants to play with
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${user_balance}")
