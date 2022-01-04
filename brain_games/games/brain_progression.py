#!/usr/bin/env python3
from brain_games.scripts import engine


def main():
    task_text = 'What number is missing in the progression?'
    engine.welcome(task_text)
    name = engine.name
    number_question = 3
    count = 0
    while count < number_question:
        engine.random_numbers()
        number_first = engine.random_number_from_1_to_49
        number_last = engine.random_number_from_50_to_1000
        random_number_for_random_progression = engine.random_number_fom_2_to_6
        numbers_list = range(number_first, number_last, random_number_for_random_progression)
        num = list(numbers_list)
        question_symbol = engine.random_number_from_0_to_9
        if num == num:
            num[question_symbol] = '..'
        task = '{} {} {} {} {} {} {} {} {} {}'.format(num[0], num[1], num[2], num[3], num[4], num[5], num[6], num[7], num[8], num[9])
        engine.question(task)
        correct_answer = str(list(numbers_list)[question_symbol])
        if engine.answer == correct_answer:
            print('Correct!')
            count += 1
        elif engine.answer != correct_answer:
            print("'{}' {} '{}'.\n{}, {}!".format(engine.answer, "is wrong answer ;(. Correct answer was", correct_answer, "Let's try again", name))
            return False
    print('{}, {}!'.format("Congratulations", name))


if __name__ == '__main__':
    main()
