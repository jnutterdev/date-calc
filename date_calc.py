'''
simple date calculator
'''

from datetime import date



date_format = "%m/%d/%Y"
today = date.today()
date = date(2017, 01, 01)
date_today = today - date

print(datetime.strptime(date_today))

# d1 = input("Enter date one mm/dd/yyyy: ")
# d2 = input("Enter date two mm/dd/yyyy: ")

# date_one = date(d1, format)
# date_two = date(d2, format)

# delta = date_one - date_two
# print(delta.days)

