import random
import prompt
from brain_games.cli import welcome_user

def primeGame():
    name = welcome_user()
    prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,97,101]
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    for _ in range(3):
        random_numbers = random.randint(1, 101)
        print(f'Question: {random_numbers}')
        answer = prompt.string('Your answer: ').strip().lower()
        if random_numbers in prime_numbers:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:  
            print('Correct!')
            score += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        if score == 3:  
            print(f'Congratulations, {name}!')


        
        












def main():
    primeGame()


if __name__ == '__main__':
    main()