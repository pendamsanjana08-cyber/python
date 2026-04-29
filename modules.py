# Write a program using the math module to calculate the area of a circle

import math
radius = 7
area = math.pi * radius ** 2
print("Area of circle:", area)

# Write a program using the datetime module to calculate your age from birth year.

import datetime
birth_year = 2005
current_year = datetime.datetime.now().year
age = current_year - birth_year
print("Age:", age)

# Write a program using the calendar module to check whether a year is a leap year.

import calendar
year = 2024
if calendar.isleap(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

