"""EX.6
Exercise: 

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

Discussion:

- List indexing
- Strings are lists

"""

just_word = input("Enter the word:")

if just_word.lower() == just_word[::-1].lower():
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
