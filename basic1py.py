'''
This is just a running script mased off of w3 python exercises
https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''




# Ex2: Script to print Python version and version info
'''

import sys  # Importing the sys module to access system-specific parameters and functions

# Print the string "Python version" to the console
print("Python version")

# Print the version of Python that is currently being used
print(sys.version)

# Print the string "Version info." to the console
print("Version info.")

# Print detailed version information as a tuple
print(sys.version_info)
'''

# Ex3: Script to display the current date and time
'''
import datetime  # Importing the datetime module to work with date and time

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time in a readable format
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
'''

# Ex4: Script to calculate the area of a circle
'''
import math  # Importing the math module to access mathematical functions

radius = float(input("Enter the radius of the circle: "))  # Get the radius of the circle from the user

area = math.pi * (radius ** 2)  # Calculate the area of the circle using the formula πr^2

print("The area of the circle with radius", radius, "is:", area)  # Print the area of the circle
'''

# Ex5: Accept the user's first and last name and print them in reverse order with a space between them
'''
names = input("Enter your first and last name: ")  # Get the user's first and last name

# Split the user's input into a list of names
names_list = names.split()

# Reverse the order of the names in the list
names_list.reverse()

# Join the names in the list with a space between them
reversed_names = ", ".join(names_list)

print("Reversed names:", reversed_names)  # Print the reversed names
'''

# Ex6: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
'''
input_numbers = input("Enter a sequence of comma-separated numbers: ")  # Get the sequence of numbers from the user

# Split the input into a list of numbers
numbers_list = input_numbers.split(",")

# Convert the list of numbers into a tuple
numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)  # Print the list of numbers
print("Tuple:", numbers_tuple)  # Print the tuple of numbers
'''

# Ex7 Write a Python program to accept a filename from the user and print the extension of that.
'''
file_name = input(" Please enter the filename: ")  # Get the filename from the user

file_split = file_name.split(".")  # Split the filename into a list using the dot as a separator

file_split.reverse()  # Reverse the list to get the extension as the first element

print(str(file_split[0]))  # Print the extension of the file
'''

# Ex8 Write a Python program to display the first and last colors from the following list.
'''
color_list = ["Red", "Green", "White", "Black"]  # Create a list of colors

print("First color:", color_list[0])  # Print the first color in the list

print("Last color:", color_list[-1])  # Print the last color in the list
'''

# Ex9 Write a Python program to display the examination schedule. (extract the date from exam_st_date).
'''
import string

exam_st_date = (11, 12, 2014)  # Create a tuple with the examination date

print("The examination will start from: %i / %i / %i" % exam_st_date)  # Print the examination date

print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")
'''

# Ex10 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''
s1 = input("Please enter a sample value in the form of an integer: ")

s2 = s1 + s1

s3 = s1 + s1 + s1

print(int(s1) + int(s2) + int(s3))
'''

# Ex11 Write a Python program to print the documents (syntax, description, etc.) of Python built-in function(s).
'''
function = input("Please enter the name of the function you would like to know more about: ")

print(f"Documentation for {function}(): ")
help(eval(function))

print('\n' + '='*80 + '\n')
'''

# Ex12 Write a Python program to print the calendar of a given month and year.
'''
import calendar

year = int(input("Please enter the year:"))
month = int(input("Please enter the month by number:"))

print(calendar.month(year,month))
'''
# Ex13 Write a Python program to print the following here document.
'''
here_document = """ a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

print(here_document)
'''

# Ex14 Write a Python program to calculate number of days between two dates.
'''
import datetime

d1 = input("Please enter the first date in the format YYYY-MM-DD: ")
d2 = input("Please enter the second date in the format YYYY-MM-DD: ")

date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

delta = date2 - date1

print(f"There are {delta.days} days between {d1} and {d2}")
'''

# Ex15 Write a Python program to get the volume of a sphere with radius 6.
'''
import math

radius = 6

volume = (3/4) * math.pi * (radius ** 3)

print(f"The volume of a sphere with radius {radius} is {volume}")
'''

# Ex16 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
'''
n1 = int(input("Please enter a number: "))

n2 = 17

dif = abs(n1 - n2)

if n1 > n2:
    print(dif * 2)
else:
    print(dif)
'''


