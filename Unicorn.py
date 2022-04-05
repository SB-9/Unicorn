# ask if user has played the game before
show_instructions = input("Have you played this game before: ")

# if input is yes, output is program continues
if show_instructions == "y":
    print("program continues")

# if input is no print instructions
elif show_instructions == "n":
    print("instructions")

# check for y/n
else:
    print("please enter y or n")
