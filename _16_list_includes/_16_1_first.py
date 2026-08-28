# #! СПИСОЧНЫЕ ВЛОЖЕНИЯ

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)
#?  ТО ЖЕ САМОЕ ТОЛЬКО В 2 СТРОКИ
# squares = [x ** 2 for x in range(10)]
# print(squares)

#! СПИСОК ЧЕТНЫХ КВАДРАТОВ ЧИСЕЛ

# even_squares = []
#? РЕШИЛ САМ
# for x in range(10):
#     even_squares.append(x**2)
# for i in even_squares:
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue
#? ЭТАЛОН
# for x in range(10):
#     if x % 2 == 0:
#         even_squares.append(x ** 2)
# print(even_squares)
#? В ОДНУ СТРОКУ
# even_squares = print([x ** 2 for x in range(10) if x % 2 == 0])