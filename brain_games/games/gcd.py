import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game():
    global task
    global correct_answer
    number_first = random.randint(0, 101)
    number_last = random.randint(0, 101)
    task = f"{number_first} {number_last}"
    correct_answer = str(math.gcd(number_first, number_last))
    return task
    return correct_answer
