import random
import prompt
from brain_games.cli import welcome_user

def calc():
    name = welcome_user()
    score = 0
    symbols = ['+', '-', '*']
    print('What is the result of the expression?')
    for _ in range(3):
        number = random.randint(1, 20)
        number2 = random.randint(1, 20)
        selected = random.choice(symbols)
        print(f'Question: {number} {selected} {number2}')
        otvet = int(prompt.string('Your answer: '))
        if selected == '+':
            correct_answer = number + number2
        elif selected == '-':
            correct_answer = number - number2
        elif selected == '*':
            correct_answer = number * number2
        if otvet == correct_answer:
            print('Correct!')
            score +=1
        else:
            print(f"'{otvet}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        if score == 3:  
            print(f'Congratulations, {name}!')
            





















def main():
    calc()


if __name__ == '__main__':
    main()