label_numbers = []
numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num % 2 == 0:
#         label_numbers.append("even")
#     else:
#         label_numbers.append("odd")
# print(label_numbers)

#? ВАРИАНТ КОРОЧЕ

label_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(label_numbers)