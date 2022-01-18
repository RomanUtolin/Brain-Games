import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def game():
    num_1 = random.randint(50, 101)
    num_2 = random.randint(0, 49)
    operation = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    str_operator, int_operator = random.choice(operation)
    question = f"{num_1} {str_operator} {num_2}"
    correct_answer = str(int_operator(num_1, num_2))
    return question, correct_answer
