"""EX.1
Exercise:

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)

Discussion:

- Getting user input
- Manipulating strings (a few ways)
"""
name = input("\nEnter your name: ")
age = int(input("\nEnter your age:"))
copies = int(input("\nHow many times you want to print the message: "))

print("\nHello {}!!!\nYou will turn 100 in {} years.\n".format(name, 100 - age))
#age_message = "\nHello {}!!!\nYou will turn 100 in {} years.\n".format(name, 100 - age)

repeat = copies * "\nHello {}!!!\nYou will turn 100 in {} years.\n".format(name, 100 - age)
print(repeat)
