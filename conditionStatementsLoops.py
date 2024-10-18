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
