import random
from datetime import datetime

choices = ['rock', 'paper', 'scissors']
username = input("Enter your username: ")

if username.lower() == 'exit':
    print("Exiting...")
else:
    user_score = 0
    computer_score = 0
    
    while user_score < 10 and computer_score < 10:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

        if user_choice == 'exit':
            print("Are you sure you want to exit? (Y/N)")
            yesorno = input().lower()
            if yesorno == 'y':
                print("Exiting the game...")
                break 
            elif yesorno == 'n':
                print("Please choose (Rock), (Paper), or (Scissors).")
                continue 

        while user_choice not in choices:
            print("Please choose (Rock), (Paper), or (Scissors).")
            user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        print(f"Current Score: {username} {user_score} - Computer {computer_score}")
    
    print(f"Game over! The final score is: {username} {user_score} - Computer {computer_score}")

with open('score.csv', 'a') as file:
        file.write(f"{username}, {str(datetime.now())}, {user_score}, {computer_score}\n")
