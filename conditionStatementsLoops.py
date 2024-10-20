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

