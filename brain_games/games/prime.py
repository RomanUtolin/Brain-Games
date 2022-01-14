from brain_games import engine
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game():
    global task
    global correct_answer
    task = random.randint(0, 999)
    correct_answer = 'yes' if engine.is_prime(task) else 'no'
    return str(task)
    return correct_answer
