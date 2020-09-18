'''

Move the code you previously wrote to calculate how many seconds are in a year into this file.
Then execute it as a script to see the output printed to your console.


There's 365 days in one year. 60 mins in one hour. 60 seconds in one minute.

60 seconds in one minute. 60sec * 60min = 3,600 seconds. So there's 3,600 seconds in 1 hour.

24 hours in 1 day

3,600sec * 24hours = 86,400 seconds in one day

86,400sec  * 365days  = 31,536,000 seconds in one year. Not counting leap year
'''

# print((60*60) * 24 * 365)

seconds = 60
minutes = 60
day = 24
year = 365

print((seconds * minutes) * day * year)
