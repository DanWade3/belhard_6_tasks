"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(list1: list, list2: list):
    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
    return sorted(list3, reverse=True)


print(common_numbers([1, 5, 4, 3, 2, 8, 7, 9, 10, 17], [1, 3, 13, 4, 5, 9, 32, 22, 10, 17]))
