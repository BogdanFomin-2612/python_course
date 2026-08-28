#       ! function Print

# print ("Hello, World!")
# print ("Hello", "World!", sep = ", ")
# print ("first row")
# print ("second row")

#       ! function Input

# name = input("Enter your name: ")
# print(name)

#       ! Переменные 

# name1 = "Alice"
# age1 = 25
# name2, age2 = "Gregor", 25
# print(name1, age1)
# print(name2, age2)

# name = "Alice"
# other_name = name
# print(other_name)

# x = 3
# y = 4

# x, y = y, x
# print(x, y)

# variable = 1
# print(type(variable))

#       ! Числа (int, float)

# my_integer = 10
# my_float = 10.5

# sum = my_integer + my_float
# umn = my_integer * my_float
# delen = my_integer / my_float
# razn = my_integer - my_float
# stepen = my_integer ** my_float
# celochislennoe = my_integer // my_float
# ostatok = my_integer % my_float

# print (sum, umn, delen, razn, stepen, celochislennoe, ostatok)

#       ! Задачка с подъеездами и этажами 00:16:48

# flat_number = 24
# entrance_number = (flat_number - 1) // 20 + 1
# floor_number = ((flat_number - 1) % 20 // 4) + 1
# print(entrance_number, "Подъезд")
# print(floor_number, "Этаж")

#       ! BOOL Булевый тип

# is_student = True
# is_graduate = False
# print(is_student, is_graduate)

# x = 10
# y = 9
# is_equal = (x == y)
# not_equal = (x != y)
# print(is_equal)
# print(not_equal)

#?      == Равно
#?      != Не Равно
#?      > Больше
#?      < Меньше
#?      >= Больше либо Равно
#?      <= Меньше либо Равно

# x = 10
# y = 9
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# x = 1
# print (x < 5 or x > -2)
# print (x < 5 & x > -2)

# ////////////////////////////

# is_student = True
# print(not is_student)

# print(bool(1))
# print(bool(0))
# print(bool(-1))
# print(bool("Hello, World!"))
# print(bool(""))

#! УСЛОВНЫЕ ОПЕРАТОРЫ

# if True:
#     print("Hello, World!")
# if False:
#     print("Not Hello, World!")

# x = 10
# if x > 0:
#     print("X is positive")
# elif x == 0:
#     print("X is Zero")
# else:
#     print("X is negative")

# x = 10
# y = 20
# if x > 0 and y > 0:
#         print("X and Y are positive")

# message = "Hello, World"
# if message:
#     print("Message is not empty")
# else: print("Message is empty")

#! ПРОВЕРКА ВЫСОКОСНОГО ГОДА

# year = 2004

# if year % 4 == 0 and year % 100 != 0:
#     print("Year is leap")
# elif year % 400 == 0 :
#     print("Year is leap")
# else: 
#     print("Year is not leap")

#! СТРОКИ (str)

# my_string = "Hello, World!"
# my_string2 = 'Hello, World! 2'
# print(my_string, my_string2)

# my_string3 = """jhbjhebihs iu esiuFHeiushfiuhsiu hauishfiuhesiufh uifehiuh iuhiu hseiuhiufhiush iuh iuh iuhuihiuh iuh iuhiuh iuhiuh iuHFUIhpsIF hsIUP Hfiupsh fiusH UIhsIUPF Hefiuphiu HIUP huph IPH iuPH IPUhiupfHiu phiuHfu ipHuifh iuhs iuhiu hius hIUH iushfiu hsIU Hiuh shf iusfhlisuh ifulshiu hiufh iulh iufhish iluhfisuh iefhiu hsiuf huse fhiueshui fhsiufh iluewsfhhesui fhi"""
# print(my_string3)

# first_name = "Alice"
# last_name = "Smith"
# full_name = first_name + " " + last_name
# print(full_name)
# print(len(full_name))


#* ЗАМЕНА КЛАССОВ

# my_integer = 100
# my_string = str(my_integer)

# print(type(my_string))

# my_int = int(my_string)
# print(type(my_int))

#! ЗАДАЧА: Найти количество цифр в ответе уравнения 2 ^ 1000

# big_int = 2 ** 1000
# print(len(str(big_int)))

# //////////////////////////////////////////

# my_string = "Hello, World!"
# print("Hello" in my_string)     #* ПОИСК СЛОВА\БУКВЫ\ЗНАЧЕНИЯ В СТРОКЕ

# my_string = "Alice"
# print(my_string.upper())        #* ИЗМЕНИТЬ ТЕКСТ НА КАПСОВЫЙ
# print(my_string.lower())        #* НАОБОРОТ ИЗМЕНИТЬ ТЕКСТ НА МАЛЕНЬКИЕ БУКВЫ

# my_string = "         Hello, World!       "
# print(len(my_string))
# print(my_string)
# print(len(my_string.strip()))
# print(my_string.strip())


# my_str = "Hello, World!"
# print(my_str.replace("World", "Python"))
# print(my_str.count("rl"))

#!  Определить: в строке цифры или нет

# my_str = "10x"
# print(my_str.isdigit())

# integer = int(input("Enter a number: "))  #? НЕПРАВИЛЬНО

# integer = input("Enter a number: ") #* ПРАВИЛЬНО
# if integer.isdigit():
#     integer = int(integer)
# print(type(integer))

#! ФОРМАТИРОВАНИЕ

# name = "Alice"
# age = 25
# print(f"Hello, my name is {name}, and I'm {age}")

#! Пользователь вводит строковое значение, а мы ему говорим, что надо вводить только числа, если не получается отформатировать нам самим.

# my_str = input("Enter a number: ")

# if my_str.isdigit():
#     my_int = int(my_str)
#     print(my_int)
# else: 
#     print("Syntax error. Your string is not a number!")
