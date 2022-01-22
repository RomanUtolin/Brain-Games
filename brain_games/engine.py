from brain_games import cli
import prompt


ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


def run_game(game):
    print(GREETING)
    name = cli.welcome_user()
    print(game.DESCRIPTION)
    for _ in range(ROUNDS):
        question, correct_answer = game.game()
        print(f"Question: {question}")
        answer = prompt.string('You answer: ')
        if answer != correct_answer:
            text = f"'{answer}' is wrong answer ;(. " \
                f"Correct answer was '{correct_answer}'.\n" \
                f"Let's try again, {name}!"
            print(text)
            return
        else:
            print('Correct!')
    print(f"Congratulations, {name}!")
