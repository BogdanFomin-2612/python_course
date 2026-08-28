#                           ЦИКЛ FOR



#* ЦИКЛ 1 (ФАЙЛЫ)
# file_names = ["doc1.txt", "image1.jpg", "doc2.txt", "image2.jpg"]

# for file_name in file_names:
#     print(file_name)



#* ЦИКЛ 2 (СТРОКИ)
# greeting = "Hello, World!"

# for char in greeting:
#     print(char)



#* ЦИКЛ 3 (СЧИТАЕМ БУКВЫ О)
# greeting = "Hello, World!"
# count_o = 0
# for char in greeting:
#     if char == "o":
#         count_o = count_o + 1       #! Либо же |count_o += 1|
#         # print(char)   #* ПРОВЕРКА
# print(count_o)



#* ЦИКЛ 4 (ВЛОЖЕНЫЕ ЦИКЛЫ)
# students = ["Alice", "Bob", "Charlie", "David"]

# for student in students:        #* Сначала полное имя одного студента
#     print(student)
#     for char in student:        #* Потом каждая буква имени этого студента
#         print(char)



#* CONTINUE & BREAK В ЦИКЛЕ
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for num in numbers:       #* CONTINUE
#     if num % 2 == 0:
#         continue
#     print(num)
    
# for num in numbers:         #* BREAK
#     if num == 10:
#         break
#     print(num)



