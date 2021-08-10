"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    n = n / 2.0
    if n == 1:
        return True
    if n == 2:
        return True
    elif n > 2:
        return check_number(n)
    else:
        return False


for n in range(50):
    print(str(n), check_number(n))
