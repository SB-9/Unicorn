"""number checker script for lucky unicorn version 3"""


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


# Main routine
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with ${user_balance}")
