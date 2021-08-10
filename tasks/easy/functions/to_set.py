"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(new_list: list):
    new_list = set(new_list)
    return print(new_list, len(new_list))


to_set([1, 2, 3, 4, 5, 6, 7])
