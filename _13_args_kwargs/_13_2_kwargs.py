#
#! KWARGS обозначаются Именованные Аргументы

# def introduce(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     # print(kwargs)
#     # print(type(kwargs))

# person = {
#     "city": "New York",
#     "age": 30,
#     "name": "John"
# }

# introduce(**person)

#? Функция которая принимает абсолютно любые значения аргументов

def func_with_all_args(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(*args)
    print(value)
    print(**kwargs)

person = {
    "city": "New York",
     "age": 30,
     "name": "John"
}

# func_with_all_args(x=1, y=2, args=1,2,3, **person) #! Какая-то хуйня