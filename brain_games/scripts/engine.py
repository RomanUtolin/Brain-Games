#!/usr/bin/env python3
import prompt
import random
import operator


def welcome(task_text):
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greeting = '{}, {}!'.format('Hello', name)
    print(greeting)
    print(task_text)
    return name


def question(task):
    global answer
    print('Question: ' + str(task))
    answer = prompt.string('You answer: ')
    return answer


def random_nubmers():
    random_number = random.randrange(0, 101)
    return random_number


def random_operator():
    global str_operator
    global int_operator
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    str_operator, int_operator = random.choice(operators)
    return str_operator, int_operator
