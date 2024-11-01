'''
https://www.w3resource.com/python-exercises/cybersecurity/index.php

Exercises for Cybersecurity in Python
'''

#1 Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string. 

def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

print(hash_password(input("Pleae input your password: ")))


