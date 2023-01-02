"""Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
/ — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция"."""

def arithmetic(a: int, b: int, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    else:
        raise Exception("Unknown operator")


#print(arithmetic(5, 3, '*'))

"""Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе."""

def is_year_leap(year):
    non_leap_exception = (1700, 1800, 1900, 2100, 2200, 2300)
    if year % 4 == 0 and year not in non_leap_exception:
        return True
    return False

#print(is_year_leap(2022))

"""Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата."""

def square(a):
    S = a**2
    P = 4*a
    D = a*2**0.5
    return S, P, D

#print(square(5.5))

"""Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
которому этот месяц принадлежит (зима, весна, лето или осень)."""

def season(day_of_month):
    seasons = {'summer': (6, 7, 8),
                'fall': (9, 10, 11),
                'winter': (12, 1, 2),
                'spring': (3, 4, 5)}
    for key, value in seasons.items():
        if day_of_month in value:
            return key

#print(season(1))

"""Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. 
Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя."""


def bank(a, year):
    for i in range(year):
        after_percent_added = a * 0.1
        a += after_percent_added
    print(a)
    return a

bank(1000, 7)

