import random


rules = 'What number is missing in the progression?'


def progression(start, diff, n):
    progression_list = []
    for i in range(n):
        item = start + i * diff
        progression_list.append(item)
    return progression_list


def hide(pr_list, n):
    elem_for_hide = random.randint(0, n - 1)
    what_hidden = str(pr_list[elem_for_hide])
    pr_list[elem_for_hide] = '..'
    pr_list_str = ' '.join(map(str, pr_list))
    return what_hidden, pr_list_str


def generation(number_min, number_max):
    start = random.randint(number_min, number_max)
    diff = random.randint(number_min, number_max)
    n = random.randint(5, 10)
    pr_list = progression(start, diff, n)
    hide_elem, prog = hide(pr_list, n)
    correct_answer = str(hide_elem)
    return prog, correct_answer
