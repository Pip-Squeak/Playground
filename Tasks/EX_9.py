"""EX.9
Exercise:

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons from 
the very first exercise)

EXTRAS:

- Keep the game going until the user types “exit”
- Keep track of how many guesses the user has taken, and when the game ends, print this out.

Discussion:

- Modules
- Random numbers
- User input
"""
import random

# Generating random number 1-9
random_number = random.randint(1,9)

# Greeting message
user_name = input("\nYour name is: ")
print(f"WELCOME to guessing game {user_name}")

# Defined if user wants to exit
users_will = ''
# counting the tries
count = 0

# Looping game till user will not tired
while users_will != "EXIT":
    # Try calculator
    count += 1
    
    # Users number
    guess_number = int(input("\nGuess the number from 1 to 9: "))

    # Game section
    if guess_number == random_number:
        print(f"\nCongratulations!!!\nYour number:\n{guess_number}\nRandom number:\n{random_number}\n")
    elif guess_number > random_number:
        print(f"\nToo high!!!\nTry again.\nRandom number is:\n{random_number}\n")
    elif guess_number < random_number:
        print(f"\nToo low!!!\nRandom number is:\n{random_number}\n")
    else: print("\nWRONG INPUT!!!")

    # Users way to stop the game
    users_will = input(f"\nTry number: {count}\nIf you want to stop, type\nEXIT\nIf you want to try again, type\nGO: ")
    if users_will.upper() == "EXIT":
        break