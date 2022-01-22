import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def game():
    num_1 = random.randint(50, 101)
    num_2 = random.randint(0, 49)
    operation = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    symbol, operators = random.choice(operation)
    question = f"{num_1} {symbol} {num_2}"
    correct_answer = operators(num_1, num_2)
    return question, str(correct_answer)
