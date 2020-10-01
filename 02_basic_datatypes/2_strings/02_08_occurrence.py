'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4
'''


# take in a string of words from the user

words = input("Enter your words: ")

# take in a letter from the user

letter = input("Pick a letter: ")

# Find the index of the first occurrence of the letter in the string

count = words.find(letter)

# print result

print(count)
