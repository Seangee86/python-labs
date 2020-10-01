'''
Write a script that prints the total number of vowels that are used in a user-inputted string.

CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?
'''


# take in a string of words from the user
string = input("Enter a word or sentence: ")

# what are the vowels in the string
vowels = 0
string = string.lower()

# count the vowels in the string
vowels += string.count("a")
vowels += string.count("e")
vowels += string.count("i")
vowels += string.count("o")
vowels += string.count("u")

# print the results
print(vowels)





