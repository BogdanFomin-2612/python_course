

def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

# print(add_all(1,2,9))


values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all(*values, *other_values))      #? Со знаком * Потому что складываем не числа а массивы чисел
