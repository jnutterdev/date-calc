from datetime import datetime, timedelta

days_to_subtract = int(input("How many days you want? "))

def get_the_days():
    d = datetime.today() - timedelta(days=days_to_subtract)
    print(d)

get_the_days()
