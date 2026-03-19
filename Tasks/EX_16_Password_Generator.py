"""EX.16
Exercise:

Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
"""
import random
import string

# Random pasword generator with symbols, digits, uppercase letters and lowercase letters
def password_generator (length = 8):
    mixed_let_dig = string.ascii_lowercase + string.digits

    mixed_characters_length = random.choices(mixed_let_dig, k=length) + random.choices(string.punctuation, k=1) + random.choices(string.ascii_uppercase, k=2)
    random.shuffle(mixed_characters_length)
    password = "".join(mixed_characters_length)

    if len(password) >= 8:
        return password
    raise Exception ("Password must contain 8 or more characters")

rand_pass = password_generator(9)
print(rand_pass)

