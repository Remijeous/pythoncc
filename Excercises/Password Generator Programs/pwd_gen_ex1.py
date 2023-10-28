import random

# Define a list of all possible characters for the password.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Generate a random password of length 12.
password = ""
for i in range(12):
    password += random.choice(characters)