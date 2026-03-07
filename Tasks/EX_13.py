"""EX.13
Exercise:

Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
"""
# Asking user for a amount of Fibonnaci number
def users_fibonnaci (fibonnaci_number = 9):
    fibonnaci_number = int(input("\nHow many Fibonnaci numbers to generate: "))
    return fibonnaci_number

fib_range = users_fibonnaci()
# Generating Fibonnaci numbers
def fibonnaci_generator():
    a = 0
    b = 1
    result = []
    for i in range(fib_range):
        a, b = b, a + b
        result.append(b)
    return result

print(fibonnaci_generator())
