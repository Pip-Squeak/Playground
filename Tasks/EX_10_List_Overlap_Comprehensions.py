"""EX.10
Exercise:

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program works on 
two lists of different sizes. Write this in one line of Python using at least one list comprehension. 

Extras:

- Randomly generate two lists to test this

Discussion:

- List comprehensions
- Random numbers, continued
"""
import random
# Manual lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Random lists
rand_num_list1 = random.sample(range(100), 15)
rand_num_list2 = random.sample(range(100), 19)

# Option N1
common = []
for i in a:
    if i in b and i not in common: common.append(i)
        
print(common)

# Option N2
rand_common = []
for i in rand_num_list1:
    if i in rand_num_list2 and i not in rand_common: rand_common.append(i)

print(f"\nRandom List1: {rand_num_list1}\nRandom List2: {rand_num_list2}\nCommon Of Random Lists: {rand_common}")

