import random
import time

def get_user_choice():
    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        print("Enter your choice (rock / paper / scissors): ")
        user_choice = input().strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def print_choices_and_winner(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    time.sleep(1)
    print(f"Computer chose: {computer_choice}")
    time.sleep(1)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def print_final_score(user_score, computer_score):
    print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")

def ask_play_again():
    while True:
        print("\nDo you want to play again? (yes/no): ")
        play_again = input().strip().lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def play_rock_paper_scissors():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print("\nRock...")
        time.sleep(1)
        print("Paper...")
        time.sleep(1)
        print("Scissors...")
        time.sleep(0.5)

        winner = determine_winner(user_choice, computer_choice)
        print_choices_and_winner(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print_final_score(user_score, computer_score)

        if not ask_play_again():
            print("\nThank you for playing!")
            break

if __name__ == "__main__":
    play_rock_paper_scissors()

