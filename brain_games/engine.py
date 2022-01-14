import prompt
import operator
import random


ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greeting = f"'Hello', {name}!"
    print(greeting)
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        game.game()
        task = game.task
        correct_answer = game.correct_answer
        question = f"Question: {task}"
        print(question)
        answer = prompt.string('You answer: ')
        if answer != correct_answer:
            text = f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'.\n" \
                f"Let's try again, {name}!"
            print(text)
            return
        else:
            print('Correct!')
    print('Congratulations, ' + name + '!')


def random_operator():
    global str_operator
    global int_operator
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    str_operator, int_operator = random.choice(operators)
    return str_operator, int_operator


def is_prime(task):
    diviser = 2
    if task <= 1:
        return False
    while task % diviser != 0:
        diviser += 1
    return task == diviser
