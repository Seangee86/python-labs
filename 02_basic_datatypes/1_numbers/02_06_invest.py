'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest
Print the future values to the console.
'''

invest = int(input('How much are you investing?')) # $100
irate = float(input('What is the interest rate?')) #.10
irate1 = invest * irate # $10

total = irate1 + invest

print(total)


time = int(input('How many years will you be investing?'))

