#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter != 3:
        random_number = random.randint(0, 1000)
        if random_number % 2 == 0:
            check_number = 'yes'
        else:
            check_number = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        right_answer = ''
        if answer == check_number:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
            else:
                continue
        else:
            right_answer = check_number
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
            break


if __name__ == '__main__':
    main()
