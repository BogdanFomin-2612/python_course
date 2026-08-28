# my_set = {1, 2, 3, 4, 5}

# print(type(my_set))
# print(my_set)

# my_set = set()

# for i in range(5):
#     my_set.add(i)
# print(my_set)

# my_set.remove(2)
# print(my_set)

#? В SET ХРАНЯТСЯ ТОЛЬКО УНИКАЛЬНЫЕ ЕЛЕМЕНТЫ (НЕ МОГУТ ПОВТОРЯТЬСЯ)

# my_set.add(4)       #* не сработает так как в сете уже есть число 4
# print(my_set)

#? ОБЬЕДИНЕНИЕ СЕТОВ

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))             #* UNION спец.команда для обьединения сетов
# print(set1.intersection(set2))      #* Высветляет общие елементы сетов
# print(set1.difference(set2))        #* Высветляет елементы которых нет в Set2


#! ЗАДАЧА: Удаление дублей из Сета

numbers = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7]
#* unique_numbers = set(numbers)

#* print(type(unique_numbers))
#* print(unique_numbers)
#* unique_numbers = list(unique_numbers)
#* print(unique_numbers)

unique_numbers = list(set(numbers))
print(unique_numbers)