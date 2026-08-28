# #! СОРТИРОВКА ЛЮДЕЙ ТОЛЬКО ПО ВОЗРАСТУ
# 
#  people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Charlie", "age": 30}
# ]

# def sort_by_age(person: dict) -> int:
#     return person["age"]

# sorted_people = sorted(people, key=sort_by_age)
# print(sorted_people)



#! СОРТИРОВКА ЛЮДЕЙ ПО ВОЗРАСТУ + ЕСЛИ ОДИНАКОВЫЙ ТОГДА СОРТИРОВКА ПО АЛФАВИТУ

people = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 25},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30}
]

def sort_by_age_name(element: dict) -> tuple[int, str]:         #? ИСПОЛНЯЮЩАЯ ФУНКЦИЯ
    return element["age"], element["name"]                      #? ИСПОЛНЯЮЩАЯ ФУНКЦИЯ

sorted_people = sorted(people, key=sort_by_age_name)
print(sorted_people)