from def_victory import *


def victory_new():
    perc = target()

    while True:
        answer = input('Поучавствуете в исторической викторине? да/нет: ')
        if answer == 'да':
            ball, right_ball_perc = question_rulers()
            print(perc)
            print('Итого правельных ответов: ', ball)
            print('Процент правильных ответов: ', right_ball_perc, '%')
        else:
            print('end')
            break
