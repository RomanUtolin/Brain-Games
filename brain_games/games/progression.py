import random

DESCRIPTION = 'What number is missing in the progression?'


def game():
    number_first = random.randint(0, 20)
    difference = random.randint(0, 50)
    lenght = random.randint(5, 10)
    random_index = random.choice(range(lenght))
    progression = []
    for _ in range(lenght):
        progression.append(number_first + difference * _)
    question_symbol = progression[random_index]
    progression[random_index] = ".."
    correct_answer = question_symbol
    question = ' '.join(str(numbers) for numbers in progression)
    return question, str(correct_answer)
