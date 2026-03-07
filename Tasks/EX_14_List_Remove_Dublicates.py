"""EX.14
Exercise:

Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
- Write two different functions to do this - one using a loop and constructing a list,
and another using sets.
"""

# list with dubs.
list_a = [1, 2, 5, 2, 6, 9, 1, 35, 19, 2, 27, 99, 35]

# Removing dublicates with for loop
def dub_remover_for_loop(list_with_dubs):
    list_without_dub = []
    for i in list_with_dubs:
        if i not in list_without_dub:
            list_without_dub.append(i)
    return list_without_dub

print("\n===Removing dublicates by for loop===")
print(dub_remover_for_loop(list_a))

# Removing dublicates with sets
def dub_remover_set(list_without_dubs):
    dubless_list = set(list_without_dubs)
    return dubless_list

print("\n===Removing dublicates by set===")
print(dub_remover_set(list_a))
