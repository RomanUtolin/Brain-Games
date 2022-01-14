import random

DESCRIPTION = 'What number is missing in the progression?'


def game():
    global task
    global correct_answer
    number_first = random.randint(0, 50)
    number_last = random.randint(50, 999)
    random_progression = random.randint(2, 6)
    numbers_list = range(number_first, number_last, random_progression)
    num = list(numbers_list)
    question_symbol = random.randint(0, 9)
    if num == num:
        num[question_symbol] = '..'
    task = f"{num[0]} {num[1]} {num[2]} {num[3]} {num[4]} {num[5]} " \
        f"{num[6]} {num[7]} {num[8]} {num[9]}"
    correct_answer = str(list(numbers_list)[question_symbol])
    return task
    return correct_answer
