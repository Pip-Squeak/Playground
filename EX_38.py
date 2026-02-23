""" EX.38
Exercise:

Implement the same exercise as Exercise 1 
(Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old), 
except use f-strings instead of the + operator to print the resulting output message.

Discussion:

One very common operation programmers need to do is display information in the form of text output.
In Python we use the print() function for this, but we need to keep one thing in mind:
the print() function only takes strings. That means, when we want to display an integer,
we need to convert it to a string before passing it to the print() function.
When we have complicated numbers to display, this becomes burdensome.

Instead, there is a built-in Python functionality called f-strings,
short for formatted string literals that solve the problem for us!

Variables:

For me, the most common use of f-strings is to automatically display variables in a string.
The mechanism to do this is:

Put the character “f” before the " from the string
Put the variable name (or expression) between { } inside the string.
For example, the following code displays my favorite color in a sentence:

"""

def when_you_will_turn_100 (your_name = "Your name", your_age = "Your age"):
    name = input("Please eneter your name: ")
    age = int(input("Please enter your age: "))
    century_clicker = 100 - age
    try:
        return print(f"\nHello {name}!!!\nYour current age is {age}.\nYou will turn 100 in {century_clicker} years.\n")
    except ValueError:
        print("Invalid input! Please enter required information.")


when_you_will_turn_100()