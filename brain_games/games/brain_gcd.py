#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    task_text = 'Find the greatest common divisor of given numbers.'
    engine.welcome(task_text)
    name = engine.name
    number_question = 3
    count = 0
    while count < number_question:
        number_one = engine.random_nubmers()
        number_two = engine.random_nubmers()
        task = '{} {}'.format(number_one, number_two)
        engine.question(task)
        correct_answer = str(engine.divider(number_one, number_two))
        if engine.answer == correct_answer:
            print('Correct!')
            count += 1
        elif engine.answer != correct_answer:
            print("'{}' {} '{}'.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was", correct_answer, "Let's try again", name))
            return False
    print('{}, {}!'.format("Congratulations", name))


if __name__ == '__main__':
    main()
