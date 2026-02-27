"""EX.4
Exercise:

Create a program that asks the user for a number and then prints out a list of all the 
divisors of that number. (If you dont know what a divisor is, it is a number that 
divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 
has no remainder.)

"""

def users_rand_nums ():
    pass

user_num = int(input("Enter the number: "))

div_list = []

for i in range(1, user_num+1):
    if user_num % i == 0: div_list.append(i)

print(div_list)
