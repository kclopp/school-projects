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

