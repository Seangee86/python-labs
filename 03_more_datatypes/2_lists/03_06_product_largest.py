'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)
'''

# user enters the number of elements to put in list
count = int(input("How many numbers? "))

# create an empty list, place the numbers in the list
my_list = []

# iterating till count to append all input elements in list
for n in range(count):
    number = int(input("Enter a number: "))
    my_list.append(number)

# find the largest number in the list, print the results
print("Largest number", max(my_list))