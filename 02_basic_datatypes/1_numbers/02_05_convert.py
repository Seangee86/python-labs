'''
Demonstrate how to:
    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.
'''
# Convert an int to a float
num = 123
print(num, "is of type", type(num))

num = float(num)
print(num, "is of type", type(num))


# Convert a float to an int
numf = 43.5
print(numf, "is of type", type(numf))
numf = int(numf)
print(numf, "is type of ", type(numf))
