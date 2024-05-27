# Write 'hello world' to the console 
print('Hello, World!')
# create game logic for a rock, paper, scissors game
# Path: app.py
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.


# Path: app.py
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
import random

print("Welcome to Rock, Paper, Scissors Game!")
player_score = 0
computer_score = 0

while True:
    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid option. Please try again.")
        continue

    print(f"Player: {player}")
    print(f"Computer: {computer}")
# Add a quit option and then print out the player's score at the end of the game.
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Final Scores:")
        print(f"Player: {player_score}")
        print(f"Computer: {computer_score}")
        break