#* RANGE В ЦИКЛЕ
# range_obj = range(10)
# print(range_obj)



# numbers = list(range_obj)         #* Вывод всех чисел диапозона
# print(numbers)



# my_range = range(3, 12)           #* Range в заданом диапозоне
# print(list(my_range))



# my_range = range(1, 10, 2)        #* Range в заданом диап. c шагом в 2 числа
# print(list(my_range))



# my_range = range(10, 1, -1)         #* Отзеркаленый список
# print(list(my_range))



# numbers = [10, 11, 12, 13, 14, 15]      #* УВЕЛИЧИТЬ КАЖДОЕ ЧИСЛО СПИСКА НА 1
# for i in range(len(numbers)):           #? i - ЭТО INDEX
#     numbers[i] += 1
# print(numbers)





#! НЕПРАВИЛЬНО

#!greetting = "Hello, World!"
#! for letter in greetting:
#!     count_o = 0
#!     for i in letter:
#!         i =+ 1
#!         if letter == "o":
#!             count_o += 1
#!             print("o", "+", i)
#! print(count_o)

#? ПРАВИЛЬНО

#? greetting = "Hello, World!"
#? indexes = []
#? count = 0

#? for i in range(len(greetting)):
#?     if greetting[i] == "o":
#?         count += 1
#?         indexes.append(i)
#? print(count)
#? print(indexes)



#! HOMEWORK СДЕЛАЛ СААААААММММ!!!!!!!!!
for i1 in range (1, 10):
    for i2 in range(1, 10):
        print(i1, " X ", i2, " = ", i1*i2)




#! ЗАКОНЧИЛ НА 01:39:58