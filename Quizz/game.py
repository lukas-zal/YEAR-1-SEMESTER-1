import random
import json
import requests

with open('users.json', 'r') as file:
    users = json.load(file)

print("Welcome to Quizz Game...")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print(f"Welcome back, {username}!")
    play_again = True
    while play_again:
        url = "https://opentdb.com/api.php?amount=5&type=multiple"
        response = requests.get(url)
        questions = response.json()['results']      

        score = 0
        q = 0

        while q < 5:
            question_info = questions[q]
            question_text = question_info['question']
            correct_answer = question_info['correct_answer']
            incorrect_answers = question_info['incorrect_answers']
            options = incorrect_answers + [correct_answer]
            random.shuffle(options)


            print(f"Question {q+1}: {question_text}")
            for i, option in enumerate(options):
                    print(f"({i + 1}) {option}")  # edo boithise to chatgpt giati den mporousa na deikso ta options

            while True:
                answer = input("Your answer: ")

                if answer.lower() == 'exit':
                    print("Are you sure you want to exit? (Y/N)")
                    yesorno = input().lower()
                    if yesorno == 'y':
                        print("Exiting the game...")
                        break
                    elif yesorno == 'n':
                        print("Please choose (1), (2), (3) or (4).")
                        continue
                    else:
                        print("Invalid input.")
                        continue
                elif answer == "1" or answer == "2" or answer == "3" or answer == "4":
                    if options[int(answer) - 1] == correct_answer:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {correct_answer}")
                    q += 1
                    break
                else:
                    print("Invalid input! Please enter a number between 1 and 4 or 'exit'.")
                    continue

            if answer.lower() == 'exit':
                break   

        print(f"Your score is: {score}/5")       

        with open('quiz_results.txt', 'a') as result_file:
            result_file.write(f"User: {username}, Score: {score}/5\n")


        play = input("Do you want to play again? (Y/N): ").lower()
        while play not in ['y', 'n']:
            print("Invalid character type (Y) or (N)")
            play = input("Do you want to play again? (Y/N): ").lower()
        if play == 'y':
            continue
        elif play == 'n':
            play_again = False
            break             

else:
    print("Invalid username or password...")
