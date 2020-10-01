'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest
Print the future values to the console.
'''



invest_amount = int(input("How much are you investing? "))

interest_rate = float(input("what's the interest rate? "))

years_investing = int(input("number of years youre  invest? "))

# invest_amount = 1000.0
# interest_rate = .007
# years_investing = 25.0

compound_interest = invest_amount * (interest_rate + 1.0) ** years_investing - invest_amount

print(compound_interest + invest_amount)

# amount_earned = invest_amount * interest_rate  # $10.00
# total_earnings = amount_earned + invest_amount  # $110
# Compound Interest=P×(1+r)** t - P
# where:
# P=Principal amount
# r=Annual interest rate
# t=Number of years interest is applied








