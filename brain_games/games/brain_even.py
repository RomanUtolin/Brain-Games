#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    task_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.welcome(task_text)
    name = engine.name
    number_question = 3
    count = 0
    while count < number_question:
        task = engine.random_nubmers()
        engine.question(task)
        if engine.answer == 'yes' and (task % 2) == 0:
            print('Correct!')
            count += 1
        elif (engine.answer == 'no' and (task % 2) != 0):
            print('Correct!')
            count += 1
        elif engine.answer == 'yes' and (task % 2) != 0:
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'no'", "Let's try again", name))
            return False
        elif engine.answer == 'no' and (task % 2) == 0:
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'yes'", "Let's try again", name))
            return False
        elif engine.answer != 'no' or 'yes':
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'yes' or 'no'", "Let's try again", name))
            return False
    print("{}, {}!".format('Congratulations', name))


if __name__ == '__main__':
    main()
