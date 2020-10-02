'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1
'''

# create empty list
num_list = []

# read in 10 numbers from the user
for a in range(1, 11):                           # gives you 1 through 10
    number = int(input("Enter in a number: "))   # number = asks user "Enter in a number" 10 times
    num_list.append(number)                      # adds users input to the list() variable "my_list"

# print result
print(num_list[1:11:2])
print(num_list[-2:-11:-2])

