import random


def perc():
    pers = input('Введите своё имя: ')
    return pers


def target():

    print('Доброго времени суток,', perc(), ', это историческая викторина')
    print('Вам будет предложено вспомнить дату вступления во власть правителей ХХ века')

    return


def random_rulers():
    """

    :return: выбор рандомной персоны
    """
    RULERS_PEOPLE = {'Николай II Александрович Романов': '01.11.1894', 'Керенский А.Ф.': '20.06.1917',
                     'Ленин В.И.': '09.11.1917', 'Сатлин И.В.': '03.04.1922', 'Хрущев Н.С.': '07.09.1953',
                     'Брежнев Л.И.': '14.10.1964', 'Андропов Ю.В.': '12.11.1982', 'Черненко К.У.': '11.04.1984',
                     'Горбачев М.С.': '15.03.1985', 'Ельцин Б.Н.': '25.12.1991'}

    name, date = random.choice(list(RULERS_PEOPLE.items()))

    return name, date


def question_rulers():
    ball = 0
    rounds = int(input('Введите количество раундов до 10: '))
    for i in range(rounds):
        name, date = random_rulers()
        answer = input(f'Когда вступил во власть - {name} ?')

        if answer == date:
            print('Верно')
            ball += 1
        else:
            print('Не верно')
    right_ball_perc = ball*100 / rounds

    return ball, right_ball_perc

