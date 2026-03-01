"""EX.11
Exercise:

Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.

Discussion:
- Functions
- Reusable functions
- Default arguments

"""
# shut the program after the result
import sys

# Simple function, just asking for a number with a default argument
def users_num (text_input = "\nGive me a number: "):
    return int(input(text_input))

# reusing the function and changing the argument
user_number = users_num("Your number is: ")

# If prime, exit and print the message; If not prime, exit and print the message.
for i in range (2, user_number):
    if user_number % i != 0:
        continue 
    elif user_number % i == 0:
        sys.exit(f"\n{user_number} is not prime.\n")

sys.exit(f"\n{user_number} is prime.\n")
