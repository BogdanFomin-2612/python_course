numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[0:5])                   #* Выписать елементы с нулевого по пятый (ВЫБОРКА)
new_numbers = numbers[0:5]              #* Всегда в выборке первый индекс входит в список а последний нет (индекс 0 будет, индекс 5 нет, последний напечатается индекс 4)
# print(new_numbers)                    #* Как в математике [0, 5)
#! Чтоб напечатать полный список надо ввести:
new_numbers2 = numbers[0:len(numbers)]
# print(new_numbers2)
new_numbers3 = numbers[0:10:2]          #* Дополнительное :2 значит что хочу вывести каждое второе число из разреза 0:10
# print(new_numbers3)

str = "Hello, World!"
# print(str[0:len(str):2])              #? Так же можно использовать print(str[::2])

#! Все варианты как можно отзеркалить список:
reversed_numbers = numbers[::-1]        #* 1 Вариант 
# print(reversed_numbers)

reversed_numbers2 = list(reversed(numbers))  #* 2 Вариант
print(type(reversed_numbers2))
print(reversed_numbers2)