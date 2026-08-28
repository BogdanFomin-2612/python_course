fruits = ["apple", "banana", "cherry", "watermelon"]
# print(fruits[1])            #! Напечатать елемент данного индекса (в данном случае индекс = 1)

# fruits[0] = "coconut"       #! Присвоение индекса елементу coconut, то есть coconut вытискает apple из своего места
# print(fruits)

fruits[0], fruits[3] = fruits[3], fruits[0]     #! Замена местами елементов
print(fruits)