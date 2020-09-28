'''
If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)
'''
miles = float(input("How many miles did you run?"))

time = float(input(f"How long did it take you to run {miles} miles?"))
  
mph = miles / time

kilo = round(mph * 1.6, 1)
#kilo = mph * 1.6

print(f"your average speed was {kilo} Kilometers")


