'''
Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay
'''

# take in user's name
name = input("What is your name? ")

# move first letter to the end. Add "ay" to the end
pig = name[1:] + name[0] + "ay"

# make  a variable

# pig =

# user name comes back sean

# use slice []

# "sean" to "ean" name[1:] you will get all but the first char "ean"

# concatenate name[1:] "ean" to name[0] "s"

# name[1:] + name[0] "eans"

# concatenate again "ay"

# pig = name[1:] + name[0] + "ay"

# print result
print(pig)


