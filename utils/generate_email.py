from random import randint


def email_generate():
    generate = randint(1, 1000)
    email = f'justin{generate}@gmail.com'
    return email
