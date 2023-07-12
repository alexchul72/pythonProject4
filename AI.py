from random import choice

answers = [

    'Конечно',
    'Думаю, да',
    'Возможно',
    'Нет',
    'Вряд ли',

    'Штундер Штундер'
]


def generate_answer():
    return choice(answers)
