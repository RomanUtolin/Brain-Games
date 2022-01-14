from brain_games import engine
import random


DESCRIPTION = 'What is the result of the expression?'


def game():
    global task
    global correct_answer
    number_first = random.randint(50, 101)
    number_last = random.randint(0, 49)
    engine.random_operator()
    operator_for_string = engine.str_operator
    operator_for_int = engine.int_operator
    task = f"{number_first} {operator_for_string} {number_last}"
    correct_answer = str(operator_for_int(number_first, number_last))
    return task
    return correct_answer
