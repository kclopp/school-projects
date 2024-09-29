# Bassed on exercises found at https://www.w3resource.com/python-exercises/puzzles/index.php

# 1 Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
'''
def check_nums(nums):
    print(nums)
    return nums.count(19) == 2 and nums.count(5) >= 3
    
print(check_nums([5, 5, 5, 19, 19, 19, 5, 5, 5, 5, 5])) # True
print(check_nums([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # False
print(check_nums([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 19])) # False
print(check_nums([5, 5, 5, 5, 5, 5, 5, 5, 5, 19, 19])) # True
'''

# 2 Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list. Otherwise return False.
'''
intList = input("Enter a list of integers: ").split()

if len(intList) == 8 and intList.count(intList[4]) == 3:
    print(True)
else:
    print(False)
'''

# 3 Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34. Return True if it meets the conditions, otherwise return False.
'''
n1 = int(input("Enter an integer: "))

if n1 > 4**4 and n1 % 34 == 4:
    print(True)
else:
    print(False)
'''



