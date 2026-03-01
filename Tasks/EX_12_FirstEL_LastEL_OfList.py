"""EX.12
Exercise:

Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list
of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

import random
 

# Users input will generate random list and prints the list
# plus prints first element of the list and last element of the list
def first_last_elem (txt_input = "Give a nuumber: ", num_len = 5):
    txt_input = int(input(txt_input))
    rand_list = random.sample(range(1, txt_input), num_len)
    print(f"\nRandom List:\n{rand_list}")
    first_last_elem = print(f"\nFirst element: {rand_list[0]}\nLast element: {rand_list[-1]}\n")


first_last_elem("Type any number: ", 7)
