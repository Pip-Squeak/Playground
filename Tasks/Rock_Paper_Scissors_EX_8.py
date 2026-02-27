"""EX.8
Exercise:

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message
 of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock

Concepts for this task:

- While loops
- Infinite loops
- Break statements
"""
# Asking 2 users for the shape and comparing them.
def players ():
    
    player_1 = input("First player: Rock/Paper/Scissors: ")
    player_2 = input("Second player: Rock/Paper/Scissors: ")
    
    if len(player_1) == len(player_2):
        print("\nTIE")
    elif len(player_1) > len(player_2):
        print ("\nCongratulations!!!\nThe winner is:\nFirst Player")
    elif len(player_1) < len(player_2):
        print ("\n\nCongratulations!!!\nThe winner is:\nSecond Player")
    else:
        print("\nIncorrect input!!!")
    

# If user wills to play again or break it
def play_again ():

    print("\n===WELCOME TO THE RPS GAME===\n")
    players()

    game = True

    while game is not False:

        user_decision = input("\nPLAY AGAIN:\n'YES' OR 'NO': ")

        if user_decision == "yes".lower():
            players()
        else:
            break

play_again()


