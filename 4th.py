__author__ = 'Мишин Егор Олегович'

'''
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''

'''
 левое делить на -2
'''


def sum_el(n, num=1):
    if n == 1:
        return num

    elif n > 1:
        return f'{num} {sum_el(n - 1, num / (-2))}'

print(sum_el(200))
