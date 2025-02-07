"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers(n):
    for i in range(n):
        yield 1 / 2 * i * (i + 1)


tn_gen = triangular_numbers(10)
for _ in range(10):
    print(next(tn_gen))
# print(next(triangle))
# print(next(triangle))
# print(next(triangle))
# print(next(triangle))
# print(next(triangle))
# print(next(triangle))
# print(next(triangle))
