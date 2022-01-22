import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    greeting = f"Hello, {name}!"
    print(greeting)
    return name
