#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    task_text = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    engine.welcome(task_text)
    name = engine.name
    number_question = 3
    count = 0
    while count < number_question:
        engine.random_numbers()
        task = engine.random_number_from_1_to_100
        engine.question(task)
        engine.is_prime(task)
        if engine.answer == 'yes' and engine.is_prime(task) is True:
            print('Correct!')
            count += 1
        elif engine.answer == 'no' and engine.is_prime(task) is False:
            print('Correct!')
            count += 1
        elif engine.answer == 'yes' and engine.is_prime(task) is False:
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'no'", "Let's try again", name))
            return False
        elif engine.answer == 'no' and engine.is_prime(task) is True:
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'yes'", "Let's try again", name))
            return False
        elif engine.answer != 'no' or 'yes':
            print("'{}' {}.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was 'yes' or 'no'", "Let's try again", name))
            return False
    print("{}, {}!".format('Congratulations', name))


if __name__ == '__main__':
    main()
