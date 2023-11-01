import random
from math import gcd

rules = 'Find the greatest common divisor of given numbers.'


def hcf(first_num, second_num):
    result = gcd(first_num, second_num)
    return result


def generation(number_min, number_max):
    first_num = random.randint(number_min, number_max)
    second_num = random.randint(number_min, number_max)
    union = f'{first_num} {second_num}'
    correct_answer = str(hcf(first_num, second_num))
    return union, correct_answer
