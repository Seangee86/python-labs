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

amount_earned = invest_amount * interest_rate  # $10.00

total_earnings = amount_earned + invest_amount  # $110

