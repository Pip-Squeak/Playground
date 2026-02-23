"""EX.5
Exercise:

Take two lists, say for example these two:

  list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
"""

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []
for i in list_a:
    if i in list_b and i not in new_list: new_list.append(i)

print(new_list)