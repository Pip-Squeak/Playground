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

# Removing duplicates with a for loop
def dup_remover_for_loop(list_with_dups):
    list_without_dup = []
    for i in list_with_dups:
        if i not in list_without_dup:
            list_without_dup.append(i)
    return list_without_dup

print("\n===Removing duplicates by for loop===")
print(dup_remover_for_loop(list_a))

# Removing duplicates with sets
def dup_remover_set(list_without_dups):
    dupless_list = set(list_without_dups)
    return dupless_list

print("\n===Removing duplicates by set===")
print(dup_remover_set(list_a))


