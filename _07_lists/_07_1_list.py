# fruits = ["apple", "banana", "cherry"]
# print(fruits)         #! Вывести список
# print (len(fruits))     #! Вывести длину списка
# print("banana" in fruits)   #! Есть ли этот елемент в списке?    True
# print("lemon" in fruits)    #! Есть ли этот елемент в списке?    False



# my_list = ["apple", 1, 1.5, True, [1, 2, 3]]        #! В списке могут быть любые значения
# print(my_list)



# my_list1 = [1, 2, 3]
# my_list2 = [1, 3, 2]
# my_list3 = [1, 2, 3]
# print(my_list1 == my_list2)     #! False
# print(my_list1 == my_list3)     #! True



# print(bool([]))     #! Пустой список всегда False
# print(bool([1]))    #! Не пустой список всегда True



# element1 = "apple"
# element2 = "cherry"
# element3 = "banana"
# fruits = [element1, element2, element3]       #! Сложение елементов в один список
# print(fruits)



# word = "hello"
# my_list = list(word)    #! КАЖДЫЙ ЭЛЕМЕНТ СТРОКИ ПРЕВРАЩАЕТ В ЭЛЕМЕНТЫ СПИСКА
# print(my_list)



# my_list1 = [1, 2, 3]
# my_list2 = [4, 5, 6]
# my_list3 = my_list1 + my_list2      #! Сложение списков
# print(my_list3)



# fruits = ["apple", "banana", "cherry"]
# fruits.append("watermelon")           #! Добавление елемента в конец списка
# print(fruits)



# my_string = "hello, world!"
# new_str = my_string.replace("world", "python")      #! Замена части НО ТОЛЬКО УЖЕ В НОВОЙ ПЕРЕМЕННОЙ
# print(my_string)
# print(new_str)



# fruits = ["apple", "banana", "cherry"]
# fruit = fruits.pop()        #! Убирает последний елемент списка
# print(fruits)



# fruits = ["apple", "banana", "cherry"]
# fruits2 = ["fig", "grape"]
# fruits.extend(fruits2)              #! Добавление елементов одного списка в другой список
# print(fruits)



# fruits = ["apple", "banana", "cherry"]
# fruits.reverse()            #! Развернуть список задом наперед
# print(fruits)



# my_list = [4, 6, 3, 7, 9, 8, 5, 2, 1]
# my_list.sort()                      #! Сортировка списка по возрастанию
# # my_list.sort(reverse=True)        #! Сортировка списка по убыванию
# print(my_list)



# my_str = "My name is Bogdan"
# my_list = my_str.split(" ")         #! Каждое отдельное слово строки делаем отдельным елементом списка, а " " это то, что отделяет каждое слово
# print(my_list)

# joined_str = " ".join(my_list)      #! Наоборот соединяет каждый елемент списка в строку с пробелами
# print(joined_str)



my_list = [3, 2, 6, 8, 4, 1, 5, 7, 10, 9]
print(max(my_list))         #! Находит максимальное значение из списка
print(min(my_list))         #! Находит минимальное значение из списка
print(sum(my_list))         #! Находит сумму всех элементов списка
