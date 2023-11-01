import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generation(number_min, number_max):
    number = random.randint(number_min, number_max)
    correct_answer = even(number)
    return number, correct_answer
