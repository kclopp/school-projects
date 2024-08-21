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

