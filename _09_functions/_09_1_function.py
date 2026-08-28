# numbers_1 = [1, 2, 3, 4, 5]     #? НАДО НАЙТИ СРЕДНЕЕ В ЭТОМ СПИСКЕ
# average_1 = sum(numbers_1) / len(numbers_1)
# print(average_1)

# numbers_2 = [6, 7, 8, 9, 10]     #? НАДО НАЙТИ СРЕДНЕЕ В ЭТОМ СПИСКЕ
# average_2 = sum(numbers_2) / len(numbers_2)
# print(average_2)


#!  Функции используются, чтобы не повторяться. 


# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [6, 7, 8, 9, 10]

# def find_average(numbers):
#     average = sum(numbers) / len(numbers)
#     return average                              #! ОБЯЗАТЕЛЬНАЯ КОМАНДА В КОНЦЕ ФУНКЦИИ

# average1 = find_average(numbers_1)
# average2 = find_average(numbers_2)
# print(average1, average2)



#! ФУНКЦИЯ СЧИТАЕТ КОЛ-ВО ГЛАСНЫХ В СТРОКЕ

# def count_vowels(string):
#     VOWELS = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count += 1
#     return count
# print(count_vowels("Hello, World!"))
# print(count_vowels("Python is a very powerful language!"))



#! ФУНЦИЯ "ЗАГЛУШКА" КОТОРАЯ НИЧЕГО НЕ ИСПОЛНЯЕТ

# def nothing():
#     # print("This function does nothing.")
#     pass

# nothing()



# def format_date(*, day: int, month: str):           #! * ДОБАВЛЕНА ДЛЯ ТОГО, ЧТОБ МОЖНО БЫЛО ПИСАТЬ ТОЛЬКО В ПОДОДЯЩЕМ ФОРМАТЕ А ИМЕННО КАК КРАСНЫЙ А НЕ СИНИЙ
#     return f"The date is {day} of {month}"

# print(format_date(day = 15, month = "december"))    #! ТАК МОЖНО ПИСАТЬ
# #? print(format_date(23, "december"))               #? ТАК НЕЛЬЗЯ



# def custom_greeting(*, name: str, greeting: str = "Hello. Congratulations!") -> str:
#     return f"{greeting}, {name}"
# print(custom_greeting(greeting="Huj", name="Bogdan"))
# print(custom_greeting(name="Bogdan"))



# def my_function():
#     local_var = "I'm local variable!"
#     print(local_var)

# my_function()


#? ИЗ ФУНКЦИИ ВЫТЯГИВАТЬ ДАННЫЕ ПРОСТО ТАК НЕ ПОЛУЧИТСЯ
# for i in range(3):
#     print(i)
# print(i)

#? А ВОТ НАОБОРОТ ВСТАВЛЯТЬ ПЕРЕМЕННЫЕ ИЗВНЕ В ФУНКЦИЮ ПОЛУЧИТСЯ
# variable = "I'm outside variable!"                  #! ВНЕШНЮЮ ПЕРЕМЕННУЮ ИЗМЕНЕНИЯ ВНУТРИ ФУНКЦИИ НЕ КОСАЮТСЯ

# def my_function():
#   variable = "I'm variable inside of function"      #! ВНУТРЕННЯЯ ПРЕМЕННАЯ ФУНКЦИИ ОСТАЕТСЯ ВНУТРИ
#   print(variable)

# my_function()
# print(variable)



# COMFORT_TEMP = 25

# def get_diff_from_comf(*, temperature: int) -> int:
#     return COMFORT_TEMP - temperature
# print(get_diff_from_comf(temperature=10))



DEFAULT_LVL_EXPERIENCE = 200

def is_lvled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    lvl_up = False

    if total_experience >= DEFAULT_LVL_EXPERIENCE:
        lvl_up = True

    return(lvl_up)

print(is_lvled_up(current_experience=150, gained_experience=60))    #? True
print(is_lvled_up(current_experience=150, gained_experience=-30))   #? False