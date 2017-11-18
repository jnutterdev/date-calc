#!/usr/bin/env python3

'''
simple date calculator that takes a user input for date and finds
finds the difference either in days or another date. 

'''
from datetime import datetime

date_one = input("What's the first date? ")
date_two = input("What's the second date? ")

def days_between(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    print(abs((d2 - d1).days))


days_between(date_one,date_two)