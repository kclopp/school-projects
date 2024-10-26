'''
https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

Python conditional statements and loops exercises

Purpose: Learning.
'''

#1 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''
def divisibleBy7AndMultipleOf5():
	for i in range(1500, 2701):
		if i % 7 == 0 and i % 5 == 0:
			print(i)

divisibleBy7AndMultipleOf5()
'''

#2 Write a Python program to convert temperatures to and from celsius, fahrenheit.
'''
def convertTemperature():
    temperature = input("Enter the temperature you want to convert (e.g. 32F, 100C): ")
    degree = int(temperature[:-1])
    unit = temperature[-1]

    if unit.upper() == 'C':
        result = int(round((9 * degree) / 5 + 32))
        unit = 'Fahrenheit'
    elif unit.upper() == 'F':
        result = int(round((degree - 32) * 5 / 9))
        unit = 'Celsius'
    else:
        print("Invalid input. Please enter a valid temperature.")
        return

    print(f"The temperature in {unit} is {result}.")

convertTemperature()
'''

#3 Write a Python program to guess a number between 1 to 9.
'''
def guessNumber():
    import random
    randomNumber = random.randint(1, 9)
    guess = 0
    count = 0

    while guess != randomNumber and guess != "exit":
        guess = input("Enter a number between 1 and 9: ")

        if guess == "exit":
            break

        guess = int(guess)
        count += 1

        if guess < randomNumber:
            print("Too low!")
        elif guess > randomNumber:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {count} tries.")

guessNumber()
'''

#4 Write a Python program to construct the following pattern, using a nested for loop.
'''
def mario():
    hight = int(input("Enter the hight of the pyramid: "))

    for i in range(hight):
        print("*" * i)

    for i in range(hight, 0, -1):
        print("*" * i)

mario()
'''

#5 Write a Python program that accepts a word from the user and reverse it.
'''
def reverseWord():
    word = input("Enter a word: ")
    reversedWord = word[::-1]
    print(f"The reversed word is: {reversedWord}")

reverseWord()
'''

#6 Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
def countEvenOdd():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even = 0
    odd = 0

    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"The number of even numbers is: {even}")
    print(f"The number of odd numbers is: {odd}")

countEvenOdd()
'''

#7 Write a Python program that prints each item and its corresponding type from the following list.
'''
def printType():
    data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

    for i in data:
        print(f"The type of {i} is: {type(i)}")

printType()
'''

#8 Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
def printNumbers():
    for i in range(7):
        if i != 3 and i != 6:
            print(i, end=' ')

printNumbers()
'''


