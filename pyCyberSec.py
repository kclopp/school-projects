'''
https://www.w3resource.com/python-exercises/cybersecurity/index.php

Exercises for Cybersecurity in Python
'''

#1 Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string. 
'''
def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

print(hash_password(input("Pleae input your password: ")))
'''

#2. Write a Python program that defines a function to generate random passwords of a specified length. The function takes an optional parameter length, which is set to 8 by default. If no length is specified by the user, the password will have 8 characters. 
'''
def generate_password(length=8):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print(generate_password(int(input("Please input the length of the password: "))))

print(generate_password())
'''

#3 Write a Python program to check if a password meets the following criteria:
# At least 8 characters long and
# Contains at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or &)
# If the password meets the criteria, print a message that says "Valid Password." If it doesn't meet the criteria, print a message that says "Password does not meet requirements."
'''
def passwordChecker(password):
    import re
    if len(password) < 8:
        print("Password does not meet requirements.")
    if not re.search("[a-z]", password):
        print("Password does not meet requirements.")
    if not re.search("[A-Z]", password):
        print("Password does not meet requirements.")
    if not re.search("[0-9]", password):
        print("Password does not meet requirements.")
    if not re.search("[!@#$%&]", password):
        print("Password does not meet requirements.")
    print("Password meets requirements.")

passwordChecker(input("Please input your password: "))
'''

#4 Write a Python function that takes a password as input and returns a list of common character substitutions that could be used to create a stronger password. 
'''
def get_password_variants(password):
    pass_variants = []
    substitutions = {
        'a': ['@', '4', 'A'],
        'e': ['3', 'E'],
        'i': ['1', '!', 'I'],
        'o': ['0', 'O'],
        's': ['$', '5', 'S'],
        't': ['7', 'T'],
        'z': ['2', 'Z']
    }
    
    for i in range(len(password)):
        if password[i] in substitutions:
            for sub in substitutions[password[i]]:
                pass_variant = password[:i] + sub + password[i+1:]
                pass_variants.append(pass_variant)
    
    pass_variants.append(password + '!')
    pass_variants.append(password + '123')
    pass_variants.append(password + '@')
    pass_variants.append(password + '#')
    pass_variants.append(password + '$')
    pass_variants.append(password + '%')
    pass_variants.append(password + '&')
    pass_variants.append(password + '*')
    pass_variants.append(password + '-')
    pass_variants.append(password + '_')
    pass_variants.append(password + '=')
    pass_variants.append(password + '+')    
    return pass_variants
password = input("Input your password: ")
result_variants = get_password_variants(password)
print(result_variants)
'''



