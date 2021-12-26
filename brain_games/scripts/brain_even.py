#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
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
            count = 5
        elif answer == 'no' and (question_number % 2) == 0:
            count = 6
        elif answer != 'no' or 'yes':
            count = 7
    if count == 3:
        print('Congratulations, ' + name + '!')
    elif count == 5:    
        print(answer + " is wrong answer ;(. Correct answer was 'no'.Let's try again, " + str(name) + "!")
    elif count == 6:
        print(answer + " is wrong answer ;(. Correct answer was 'yes'.Let's try again, " + str(name) + "!")
    elif count == 7:
        print(answer + " is wrong answer ;(. Correct answer was 'yes' or 'no' .Let's try again, " + str(name) + "!")
        

if __name__ == '__main__':
    main()
