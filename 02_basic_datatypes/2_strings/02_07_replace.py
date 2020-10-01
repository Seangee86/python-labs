'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please
'''

# whats the first step?
# write input to gather a string of words
string = input("String input: ")

# next step user input for a symbol
symbol = input("symbol input: ")

# Replace all occurrences of the first letter with the symbol
first_letter = string[0]
replacement = string.replace(first_letter, symbol)
# print result
print(replacement)
