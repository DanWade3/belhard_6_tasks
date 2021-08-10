"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))
