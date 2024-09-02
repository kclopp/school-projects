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

# Ex17 Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''
n1 = int(input("Please enter a number: "))

if abs(1000 - n1) <= 100:
    print("The number is within 100 of 1000")
elif abs(2000 - n1) <= 100:
    print("The number is within 100 of 2000")
else:
    print("The number is not within 100 of 1000 or 2000")
'''

# Ex18 Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
'''
n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))
n3 = int(input("Please enter the third number: "))

sum = n1 + n2 + n3

if n1 == n2 == n3:
    print(sum * 3)
else:
    print(sum)
'''

# Ex19 Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
'''
value = input("Please enter a string: ")

if value[:2] == "Is":
    print(value)
else:
    print("Is" + value)
'''

# Ex20 Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''
n1 = int(input("Please enter a non-negative integer: "))
n1 = abs(n1)

value = input("Please enter a string: ")

print(value * n1)
'''

#Ex21 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
'''
n1 = float(input("Please enter a number: "))
if n1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
'''

# Ex22 Write a Python program to count the number 4 in a given list.
'''
import random 

num_list = list()
i = 0
count = 0

while i < 100:
    i = i + 1
    num_list.append(random.randint(1,10))

for num in num_list:
    if num == 4:
        count = count + 1

print(f"The number 4 appears {count} times in the list {num_list}")
'''

# Ex23 Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
'''
n1 = int(input("Please enter a non-negative integer: "))
s1 = input("Please enter a string: ")

if len(s1) < 2:
    print(s1 * n1)
else:
    print(s1[:2] * n1)
'''

# Ex24 Write a Python program to test whether a passed letter is a vowel or not.
'''
c1 = input("Please enter a letter: ")
vowels = ['a','e','i','o','u']

if c1 in vowels:
    print("The letter is a vowel")
else:
    print("The letter is not a vowel")
'''

# Ex25 Write a Python program to check whether a specified value is contained in a group of values.
'''
valGroup = [1, 5, 8, 3]

val = int(input("Please enter a value: "))

if val in valGroup:
    print(f"The value {val} is in the group {valGroup}")
else:
    print(f"The value {val} is not in the group {valGroup}")
'''

# Ex26 Write a Python program to create a histogram from a given list of integers.
'''
listOfInt = input("Please list integers seperated by a comma ")

listOfInt = listOfInt.split(",")

for i in listOfInt:
    print("*" * int(i))
'''

# Ex27 Write a Python program to concatenate all elements in a list into a string and return it.
'''
listOfStr = input("Please list strings seperated by a comma ")

listOfStr = listOfStr.replace(" ", "")

listOfStr = listOfStr.split(",")

print("".join(listOfStr))
'''

# Ex28 Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
'''
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]

numList = []
for num in numbers:
    if num == 237:
        break
    elif num % 2 == 0:
        numList.append(num)

print(numList)

numList.sort()

print(numList)
'''

# Ex29 Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))
'''

# Ex30 Write a Python program that will accept the base and height of a triangle and compute the area.
'''
base = float(input("Please enter the base of the triangle: "))
height = float(input("Please enter the height of the triangle: "))
area = (base * height) / 2
print(f"The area of the triangle with base {base} and height {height} is {area}")
'''

# Ex31 Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
'''
n1 = int(input("Please input positave int #1 "))
n2 = int(input("Please input positive int #2 "))

if n1 > n2:
    i = n2
    while i > 0:
        if ((n1 % i) == 0) & ((n2 % i) == 0):
            print(i)
            break
        else:
            i = i - 1
else:
    i = n1
    while i > 0:
        if ((n1 % i) == 0) & ((n2 % i) == 0):
            print(i)
            break
        else:
            i = i - 1
'''

# Ex32 Write a Python program to get the least common multiple (LCM) of two positive integers.
'''
n1 = int(input("Please input positave int #1 "))
n2 = int(input("Please input positive int #2 "))

if n2 > n1:
    k = n2
    n2 = n1
    n1 = k

i = n2
while True:
    if (i % n1 == 0) & (i % n2 == 0):
        print(i)
        break
    else:
        i = i + 1
'''

# Ex33 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''
n1 = int(input("Please input int #1 "))
n2 = int(input("Please input int #2 "))
n3 = int(input("Please input int #3 "))

if n1 == n2:
    print(0)
elif n1 == n3:
    print(0)
elif n2 == n3:
    print(0)
else:
    print(n1 + n2 + n3)
'''

# Ex34 Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
'''
n1 = int(input("Please input int #1 "))
n2 = int(input("Please input int #2 "))

sum = n1 + n2

if sum >= 15 & sum <= 20:
    print(20)
else:
    print(sum)
'''

# Ex35 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''
n1 = int(input("Please input int #1 "))
n2 = int(input("Please input int #2 "))

if n1 == n2:
    print(True)
elif abs(n1 - n2) == 5:
    print(True)
elif n1 + n2 == 5:
    print(True)
else:
    print(False)
'''

# Ex36 Write a Python program to add two objects if both objects are an integer type.
'''
n1 = 1
n2 = "cat"

if type(n1) == int and type(n2) == int:
    print(n1 + n2)
else:
    print("The objects are not both integers")
'''

# Ex37 Write a Python program to display your details like name, age, address in three different lines.
'''
profile = {
    "name": "John Doe",
    "age": 30,
    "address": "123 Main St"
}

print(f"Name: {profile['name']}\nAge: {profile['age']}\nAddress: {profile['address']}")
'''

# Ex38 Write a Python program to solve (x + y) * (x + y).
'''
x = int(input("Please input x "))
y = int(input("Please input y "))

print((x + y) * (x+y))
print((x + y) ** 2)
'''

# Ex39 Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
'''
principal = float(input("Please input the principal amount "))
rate = float(input("Please input the rate of interest "))
years = float(input("Please input the number of years "))

future_value = principal * ((1 + rate) ** years)

print(f"The future value of the principal amount {principal} with a rate of interest {rate} over {years} years is {future_value}")
'''

# Ex40 Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
'''
import math

x1 = float(input("Please input x1 "))
y1 = float(input("Please input y1 "))
x2 = float(input("Please input x2 "))
y2 = float(input("Please input y2 "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")
'''

# Ex41 Write a Python program to check whether a file exists.  
'''
fileName = input("Please input the file name ")

try:
    with open(fileName, "r") as file:
        print(f"The file {fileName} exists")
except FileNotFoundError:
    print(f"The file {fileName} does not exist")
except:
    print("An error occurred")
'''

# Ex42 Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
'''
import platform

print(platform.architecture()[0])
'''

# Ex43 Write a Python program to get OS name, platform and release information.
'''
import os, platform

print(os.name)
print(platform.system())
print(platform.release())
'''

# Ex44 Write a Python program to locate Python site-packages.
'''
import site

print(site.getsitepackages())
'''

# Ex45 Write a python program to call an external command in Python.
'''
from subprocess import run

command = input("Please input the command you would like to run ")

run(command, shell=True)
'''

# Ex46 Write a python program to get the path and name of the file that is currently executing.
'''
import os

print(__file__)

print(os.path.realpath(__file__))
'''

# Ex47 Write a Python program to find out the number of CPUs using.
'''
import os

print(os.cpu_count())
'''

# Ex48 Write a Python program to parse a string to Float or Integer.
'''
s1 = input("Please input a string ")

try:
    print(float(s1))
    print(int(float(s1)))
except:
    print("The string is not a number")
'''

# Ex49 Write a Python program to list all files in a directory in Python.
'''
d1 = {}

for i in range(10):
    d1.update({i: i * 5})

print(d1)
'''

# Ex50 Write a Python program to print without newline or space.
'''
print("Hello", end="")
'''

# Ex51 Write a Python program to determine the profiling of Python progrmas.
'''
import cProfile

def sum():
    print (1+2)

cProfile.run('sum()')
'''

# Ex52 Write a Python program to print to stderr.
'''
import sys

sys.stderr.write("This is an error message\n")
'''

# Ex53 Write a python program to access environment variables.
'''
import os

print(os.getenv("PATH"))
'''

# Ex54 Write a Python program to get the current username
'''
import os

print(os.getlogin())
'''

# Ex55 Write a Python to find local IP addresses using Python's stdlib
'''
import socket

local_hostname = socket.gethostname()

local_fqdn = socket.getfqdn()

ip_address = socket.gethostbyname(local_hostname)

print(f"Local Hostname: {local_hostname}")
print(f"Local FQDN: {local_fqdn}")
print(f"IP Address: {ip_address}")
'''



