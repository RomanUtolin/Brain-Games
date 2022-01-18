import prompt


ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greeting = f"'Hello', {name}!"
    print(greeting)
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        question, correct_answer = game.game()
        print("Question: " + str(question))
        answer = prompt.string('You answer: ')
        if answer != correct_answer:
            text = f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'.\n" \
                f"Let's try again, {name}!"
            print(text)
            return
        else:
            print('Correct!')
    print('Congratulations, ' + name + '!')
