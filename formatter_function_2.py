"""Statement formatter version 3, for testing"""


# function to format the text output
def formatter(text, symbol):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("Welcome to the Unicorn Game", "-"))
print()
print(formatter("Congratulations, you got a Unicorn", "!"))
print()
print(formatter("Goodbye", "*"))
