from prompt import string


def welcome_user():
    name = string('May I have your name? ')
    if name == name:
        greeting = 'Hello, ' + str(name)
        print(greeting)
