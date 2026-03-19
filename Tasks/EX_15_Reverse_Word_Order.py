"""EX.15
Exercise: 

Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""
def reversing_string (reversed_string):
    reverse_string = " ".join(reversed_string.split()[::-1]).capitalize()
    return reverse_string


result = reversing_string("My name is Ponito")
print(result)

