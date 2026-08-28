#
#! === === СЛОВАРИ === ===
#? Первый вариант записи (удобно)
# person = {
#     "name": "Bogdan",
#     "age": 20,
#     "city": "Gdańsk"
# }
# person["job"] = "Engineer"      #* Добавил отдельно доп.категорию словаря

# print(person)

#? Второй вариант записи (неудобно)
#* Формат: ["КЛЮЧ"] = "ЗНАЧЕНИЕ"

person = {}

person["name"] = "Bogdan"
person["age"] = 20
person["city"] = "Gdańsk"
person["job"] = "Engineer"

# print(person)
# print(person["name"])
# print(person.get("name"))

# for p in person:
#     print (person[p])

# for item in person.items():
#     print(item)
#     print(type(item))

#? Итерация только по ключам

for key in person.keys():
    print(key)

#? Итерация только по значениям

for value in person.values():
    print(value)