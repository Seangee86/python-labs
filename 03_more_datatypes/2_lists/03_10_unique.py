'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]

'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
#
# unique_list = set()
#
#
# print(set(list_))

# get distinct items

items = list(set(list_))

for i in items:
    items.count(i)
if i == 1:
    print(i)






print(items)