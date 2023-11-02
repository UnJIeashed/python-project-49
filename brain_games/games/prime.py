import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def even(number):
    if number < 2:
        return 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def generation(number_min, number_max):
    number = random.randint(number_min, number_max)
    correct_answer = even(number)
    return number, correct_answer
