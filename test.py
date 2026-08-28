# #!    Задача 1. Дом с подъездами (вариант)

#!      В доме 6 подъездов по 24 квартиры, на каждом этаже — 6 квартир. 
#!      Напишите функцию get_entrance_and_floor(number), 
#!      которая возвращает кортеж (подъезд, этаж) 
#!      для произвольного номера квартиры (нумерация с единицы, как в реальной жизни).

# def get_entrance_and_floor(number, per_entrances=24, per_floors=6):
#     n = number - 1
#     entrance = n // per_entrances + 1
#     floor = (n % per_entrances) // per_floors + 1
#     return entrance, floor

# print(get_entrance_and_floor(24))


#! Задача 2. Високосный год

#! Напишите функцию is_leap_year(year) -> bool, 
#! использующую правило: год високосный, если делится на 4, 
#! но не делится на 100, либо делится на 400. 
#! Проверьте на годах 1900, 2000, 2023, 2024.

# def is_leap_year(year) -> bool:
#     if year % 4 == 0 & year // 100 != 0 & year // 400 == 0:
#         print(True)
#     else: print(False)

# print(is_leap_year(1900))
# print(is_leap_year(2000))
# print(is_leap_year(2023))
# print(is_leap_year(2024))

