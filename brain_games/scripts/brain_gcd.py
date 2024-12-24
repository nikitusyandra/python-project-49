import random
import prompt
from brain_games.cli import welcome_user
import math


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        
        print(f'Question: {num1} {num2}')
        
        user_answer = input('Your answer: ').strip()

        correct_answer = math.gcd(num1, num2) 
        if user_answer.isdigit() and int(user_answer) == correct_answer:  
            print('Correct!')
            score += 1 
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    print(f'Congratulations, {name}!')









def main():
    gcd()


if __name__ == '__main__':
    main()