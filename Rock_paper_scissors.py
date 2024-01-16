import random

print("Welcome to Rock, Paper, Scissors!")
print("You'll be playing against the computer.")

player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

while True:
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    computer_choice = random.choice(choices)

    print(f"\nYou chose {player_choice}, and the computer chose {computer_choice}.\n")

    if player_choice not in choices:
        print("Invalid input. Try again.")
        continue

    if player_choice == computer_choice:
        print("Tie")
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1

    print(f"\nCurrent score: Player {player_score} - {computer_score} Computer\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        break

print(f"\nFinal Score: Player {player_score} - {computer_score} Computer")
print("Thanks for playing!")