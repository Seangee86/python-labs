'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]
unique : if an item doesnt show up more than once
'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13, 2]

unique_list = []

# get distinct items

items = list(set(list_))

num = list_.count(6)
print(num)
