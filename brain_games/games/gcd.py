import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game():
    num_1 = random.randint(0, 101)
    num_2 = random.randint(0, 101)
    question = f"{num_1} {num_2}"
    correct_answer = _gcd(num_1, num_2)
    return question, correct_answer


def _gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return str(num_1 + num_2)
