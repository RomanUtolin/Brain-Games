import random

DESCRIPTION = 'What number is missing in the progression?'


def game():
    number_first = random.randint(0, 100)
    number_last = random.randint(200, 999)
    diff_progression = random.randint(2, 6)
    num = list(range(number_first, number_last, diff_progression))
    random_index = random.randint(0, 9)
    question_symbol = num[random_index]
    num[random_index] = '..'
    progression = num[0:10]
    correct_answer = str(question_symbol)
    progression = [str(numbers) for numbers in progression]
    question = " ".join(progression)
    return question, correct_answer
