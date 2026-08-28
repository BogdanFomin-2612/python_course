# #! СОРТИРОВКА:
#   [2, 1, 3] -> [1, 2, 3] #* ПО ВОЗРАСТАНИЮ
#
# #! ФИЛЬТРАЦИЯ:
#   [1, 2, 3, 4, 5] -> [2, 4] #* ЧЕТНЫЕ


fruits = ["banana", "apple", "cherry", "date"]

# sorted_fruits = sorted(fruits)                          #* ПО АЛФАВИТУ
# revers_sorted_fruits = sorted(fruits, reverse=True)     #* НАОБОРОТ ПРОТИВ АЛФАВИТА

# print(sorted_fruits)
# print(revers_sorted_fruits)

#? СОРТИРОВКА СЛОВ ПО ДЛИНЕ

def sort_by_len(element: str) -> int:
    return len(element)

sorted_fruits = sorted(fruits, key=sort_by_len)     #* Сортирует каждый елемент массива от большего к меньшему

print(sorted_fruits)
