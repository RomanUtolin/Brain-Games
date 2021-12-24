#!/usr/bin/env python3
import prompt
import random


if __name__ == '__main__':
    main()


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        question_number = random.randrange(0, 100)
        print('Question: ' + str(question_number))
        answer = prompt.string('You answer: ')
        if answer == 'yes' and (question_number % 2) == 0:
            print('Correct!')
            count += 1
        elif (answer == 'no' and (question_number % 2) != 0):
            print('Correct!')
            count += 1
        elif answer == 'yes' and (question_number % 2) != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.Let's try again, " + str(name) + "!")
            count = 1
        elif answer == 'no' and (question_number % 2) == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.Let's try again, " + str(name) + "!")
            count = 1
        elif answer != 'no' or 'yes':
            print("Please enter correct (yes or no).Let's try again, " + str(name) + "!")
    print('Congratulations, ' + name + '!')
