
import random
import prompt
from brain_games.cli import welcome_user

def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        otvet = prompt.string('Your answer: ').strip().lower()
        if number % 2 == 0:  
            correct_answer = 'yes'
        else:  
            correct_answer = 'no'

        if otvet == correct_answer:  
            print('Correct!')
            score += 1
        else:
            print(f"'{otvet}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    




def main():
    even_game()


if __name__ == '__main__':
    main()