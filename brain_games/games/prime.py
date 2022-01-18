import math
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game():
    question = random.randint(0, 100)
    correct_answer = 'yes' if _is_prime(question) else 'no'
    return question, correct_answer


def _is_prime(question):
    divider = 2
    if question < 2:
        return False
    if question == 2:
        return True
    while divider <= math.sqrt(question):
        if question % divider == 0:
            return False
        divider += 1
    return True
