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

#4 We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile. 
'''
n1 = int(input("Enter the number of piles: "))
n2 = n1
l1 =[]

for i in range(n1):
    l1.append(n2)
    n2 = n2 +2

print(l1)
'''

#5 Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings. Return True if the characters of the nth string are contained in the nth-1 string. Otherwise return False.
'''
def check_proper_substring(strings):
    for i in range(1, len(strings)):
        if strings[i-1] in strings[i] and strings[i-1] != strings[i]:
            print(f"'{strings[i-1]}' is a proper substring of '{strings[i]}'")
        else:
            print(f"'{strings[i-1]}' is NOT a proper substring of '{strings[i]}'")

# Example usage
strings = ["hello", "hello world", "world", "worldwide"]
check_proper_substring(strings)

strings = ["hello", "goodbye", "night", "day"]
check_proper_substring(strings)
'''

# 6 Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False. 
'''
l1 = [i for i in range(0, 1000, 10)]

l2 = [i for i in range(5, 1000, 9)]

def check_list(l0):
    if len(l0) !=100:
        return False

    for i in range(1, len(l0)):
        if l0[i] - l0[i-1] != 10:
            return False
        else:
            return True

print(check_list(l1))

print('*****************************')

print(check_list(l2))
'''

#7 Write a Python program to check a given list of integers where the sum of the first i integers is i. Return True if the list satisfies the condition, otherwise False.
'''
l1 = [1, 2, 3, 4, 5]
l2 = [1, 1, 1, 1, 1]
l3 = [2, 2, 2, 2, 2]

def check_list(l0):
    print(f"The sum of the list is {sum(l0)}")
    print(f"The length of the list is {len(l0)}")
    return(sum(l0) == len(l0))

print(check_list(l1))
print('*****************************')
print(check_list(l2))
print('*****************************')
print(check_list(l3))
print('*****************************')
'''

#8  Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
'''
def split_string(string):
    import re

    words = re.findall(r'\w+', string)
    separators = re.findall(r'\W+', string)

    print(f"Words: {words}")
    print(f"Separators: {separators}")

# Example usage

split_string("The dance, held in the school gym, ended at midnight.")
'''

#9 Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
'''
def gen_list():
    import random

    l1 = []

    while len(l1) < 20:
        n1 = random.randint(0, 100)
        if len(l1) == 0:
            l1.append(n1)
        elif l1[-1] != n1:
            l1.append(n1)

    return(l1)

def check_list(lst1):
    for i in range(len(lst1) -1):
        if lst1[i] == lst1[i+1]:
            stat = False
            print(f'{lst1[i]} is equal to {lst1[i+1]} at index {i} and {i+1}')
            break
        else:
            stat = True

    print(stat)

lst = gen_list()
print(lst)

check_list(lst)

lst2 = [25, 66, 46, 25, 10, 100, 3, 25, 14, 13, 87, 89, 7, 27, 96, 39, 39, 67, 88, 42]
print(lst2)
check_list(lst2)
'''

#10 Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace. 
'''
def split_parentheses(string):
    string = string.replace(" ", "")


    count = 0
    temp = ''
    groups = []
    
    # Iterate through the string
    for char in string:
        temp += char
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        # When count is zero, we have a balanced group
        if count == 0 and temp:
            groups.append(temp)
            temp = ''
            

    return groups

input_string = "( ()) ((()()())) (()) ()"
output_groups = split_parentheses(input_string)
print(output_groups)
'''

#11 Write a Python program to find the indexes of numbers in a given list below a given threshold. 
'''
def find_indexes(lst, threshold):
    indexes = [i for i in range(len(lst)) if lst[i] < threshold]
    return indexes

# Example usage
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
threshold = 5
indexes = find_indexes(lst, threshold)
print(indexes)
'''

#12 Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False. 
'''
def check_pal(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string == string[::-1]

print(check_pal(input("Enter a string: ")))
'''

#13 Write a Python program to find strings in a given list starting with a given prefix. 
'''
def find_strings(lst, prefix):
    strings = [string for string in lst if string.startswith(prefix)]
    return strings

# Example usage
lst = ['hello', 'world', 'python', 'programming']
prefix = 'p'
strings = find_strings(lst, prefix)
print(strings)
'''

#14 Write a Python program to find the length of a given list of non-empty strings. 
'''
def find_length(lst):
    lengths = [len(string) for string in lst]
    return lengths

# Example usage
lst = ['hello', 'world', 'python', 'programming']
lengths = find_length(lst)
print(lengths)
'''

#14 Write a Python program to find the longest string in a given list of strings.
'''
def find_longest(lst):
    longest = max(lst, key=len)
    return longest

# Example usage

lst = ['hello', 'world', 'python', 'programming']
longest = find_longest(lst)
print(longest)
'''

#15 Write a Python program to find strings in a given list containing a given substring. 
'''
def find_strings(lst, substring):
    strings = [string for string in lst if substring in string]
    return strings

# Example usage
lst = ['hello', 'world', 'python', 'programming']
substring = 'o'
strings = find_strings(lst, substring)
print(strings)
'''

#16 Write a Python program to create a string consisting of non-negative integers up to n inclusive. 
'''
def create_string(n):
    string = ''.join([str(i) for i in range(n+1)])
    return string

# Example usage
n = 5
string = create_string(n)
print(string)
'''

#17 An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
# Write a Python program to find the indices of all occurrences of target in the uneven matrix.
'''
def find_indices(matrix, target):
    indices = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == target]
    return indices

# Example usage
matrix = [[1, 2, 8], [4, 5], [6, 7, 8, 9]]
target = 8
indices = find_indices(matrix, target)
print(indices)
'''

#18


#19 Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.). 
'''
def split_string(s):
    if ' ' in s:
        return s.split(' ')
    elif ',' in s:
        return s.split(',')
    else:
        return [char for i, char in enumerate(s.lower()) if i % 2 != 0]

# Example usage
s = "a, b, c, d"

print(split_string(s))

s = "a,b,c,d"

print(split_string(s))

s = "abcd"

print(split_string(s))
'''






