import os
import random

def password_generation(length):
    # Define the characters to choose from
    characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*_"
    
    # If the length is 0 or less, return an empty password
    if length <= 0:
        return ""
    # Generate a random password using os.urandom for secure random bytes
    # Then, use random.choice to select characters based on that
    random_bytes = os.urandom(length)
    
    # Convert random bytes to characters 
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

password_length = int(input("Enter the password length: "))
password = password_generation(password_length)
print(f"Your Password is : {password}")
