from datetime import datetime

# - ask for user input
input_one = input("What's the first date? (YYYY-MM-DD) ")
input_two = input("What's the second date? (YYYY-MM-DD) ")

# convert user input into variables for date function

d0 = datetime.strptime(input_one, "%Y-%m-%d")
d1 = datetime.strptime(input_two, "%Y-%m-%d")

# - perform calculations
if (d1 > d0):
    delta = d1 - d0
else:
    delta = d0 - d1

# - print date or day
print(delta.days)
