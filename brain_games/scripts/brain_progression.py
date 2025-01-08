import random
import prompt
from brain_games.cli import welcome_user
import math

def progressionGame():
    name = welcome_user()
    print('What number is missing in the progression?')
    score = 0
    for _ in range(3):
        length = random.randint(9, 14)
        start_number = random.randint(1, 80)
        arifm = random.randint(1, 5)
        progression = [start_number + arifm * i for i in range(length)]
        hidden_index = random.randint(0, length - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'
        print("Question:", ' '.join(map(str, progression)))
        answer = prompt.string('Your answer: ').strip().lower()
        if answer.isdigit() and int(answer) == hidden_number:
            print('Correct!')
            score += 1  
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            break
    
        if score == 3:
            print(f"Congratulations, {name}! ")
        

def main():
    progressionGame()


if __name__ == '__main__':
    main()
