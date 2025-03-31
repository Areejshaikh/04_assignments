import random

def computer_move():
    options = ['Rock', 'Paper', 'Scissors']  # "Papper" کو "Paper" اور "Scissor" کو "Scissors" میں درست کیا
    move = options[random.randint(0, 2)]
    return move

def winner(computer_move, player_move):
    if computer_move == player_move:
        return 'tie'
    elif player_move == 'Rock' and computer_move == 'Paper':
        return 'computer'
    elif player_move == 'Paper' and computer_move == 'Scissors':
        return 'computer'
    elif player_move == 'Scissors' and computer_move == 'Rock':
        return 'computer'
    else:
        return 'player'

# Example Usage:
player_choice = input("Enter Rock, Paper, or Scissors: ")
computer_choice = computer_move()
print(f"Computer chose: {computer_choice}")

result = winner(computer_choice, player_choice)
print(f"The winner is: {result}")
