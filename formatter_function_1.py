"""Statement formatter version 2, converted into a function"""


# function to format the text output
def formatter(text, symbol):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
text_ = input("Enter the statement to format: ")
symbol_ = input("enter the symbol you want to use: ")
print()
print(formatter(text_, symbol_))
