#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    task_text = 'What is the result of the expression?'
    engine.welcome(task_text)
    name = engine.name
    number_question = 3
    count = 0
    while count < number_question:
        engine.random_numbers()
        number_first = engine.random_number_from_50_to_100
        number_last = engine.random_number_from_1_to_49
        engine.random_operator()
        operator_for_string = engine.str_operator
        operator_for_int = engine.int_operator
        task = '{} {} {}'.format(number_first, operator_for_string, number_last)
        engine.question(task)
        correct_answer = str(operator_for_int(number_first, number_last))
        if engine.answer == correct_answer:
            print('Correct!')
            count += 1
        elif engine.answer != correct_answer:
            print("'{}' {} '{}'.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was", correct_answer, "Let's try again", name))
            return False
    print('{}, {}!'.format("Congratulations", name))


if __name__ == '__main__':
    main()
