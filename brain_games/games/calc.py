import random


rules = 'What is the result of the expression?'
operations_list = ['+', '-', '*']


def calc(first_num, second_num, operation):
    result = eval(f'{first_num} {operation} {second_num}')
    return result


def generation(number_min, number_max):
    first_num = random.randint(number_min, number_max)
    second_num = random.randint(number_min, number_max)
    operation = random.choice(operations_list)
    union = f'{first_num} {operation} {second_num}'
    correct_answer = str(calc(first_num, second_num, operation))
    return union, correct_answer
