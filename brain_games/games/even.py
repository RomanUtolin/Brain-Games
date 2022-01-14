import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def game():
    global task
    global correct_answer
    task = random.randint(1, 101)
    correct_answer = 'yes' if task % 2 == 0 else 'no'
    return task
    return correct_answer
