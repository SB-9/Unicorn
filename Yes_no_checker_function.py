"""Lucky unicorn Yes no checker function"""


# functions go here
def yes_no(question):
    # ask if user has played the game before
    answer = input(question)

    # check for unexpected inputs
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("Please enter y or n: ")

    # check for yes
    if answer.lower() == "y":
        return "Yes"

    # others=wise show instructions
    else:
        return "No"


# main routine go here
show_instructions = yes_no("have you played the game before?: ")
print(f"you entered '{show_instructions}'")
print()
having_fun = yes_no("are you having fun?: ")
print(f"you entered '{having_fun}'")
