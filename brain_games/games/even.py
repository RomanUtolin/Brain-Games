import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def game():
    question = random.randint(1, 101)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
