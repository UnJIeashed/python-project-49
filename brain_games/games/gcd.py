import random


rules = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return str(number1 or number2)


def generation(number_min, number_max):
    first_num = random.randint(number_min, number_max)
    second_num = random.randint(number_min, number_max)
    union = f'{first_num} {second_num}'
    correct_answer = gcd(first_num, second_num)
    return union, correct_answer
