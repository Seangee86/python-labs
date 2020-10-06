'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.
'''

# string from user
#string = input("write something: ")
string2 = "You are a super super cool cat"     # temp string

# with the split() method, creates a list of each word
string_list = string2.split()

# create an empty list
word_count = []

for w in string_list:
    word_count.append(string_list.count(w))

print(string_list, word_count)

