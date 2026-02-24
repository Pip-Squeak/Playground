"""EX.2
Exercise:

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd number 
react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and
one number to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.

Discussion:
- Modular arithmetic (the modulus operator)
- Conditionals (if statements)
- Checking equality
"""

# # Extras N1
# def users_number ():
#     asked_number = int(input("Enter the number: "))

#     if asked_number % 4 == 0:
#         print("{} is multiple of 4 and is even".format(asked_number))
#     elif asked_number % 2 == 0:
#         print("{} is multiple of 2 and is even".format(asked_number))
#     else:
#         print("{} is odd".format(asked_number))

# users_number()


# Extras N2

num = int(input("Enter the divisor number: "))
check = int(input("Enter the number to divide: "))

result = num / check

if num % check == 0:
    print(f"{result} is divided evenly")
else:
    print(f"{result} doesn't divides evenly")
