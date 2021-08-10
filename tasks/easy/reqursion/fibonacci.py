"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
