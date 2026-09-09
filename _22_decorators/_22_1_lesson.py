#
#! ДЕКОРАТОРЫ - синтаксический сахар, т.е. конструкция языка, которая делает более быстрым написание каких-то чистотных паттернов.
#? Как аргумент принимает другую функцию и как-то обогощает поведение принимаемой функции

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Что то случилось до вызова функции")
#         func(*args, **kwargs)
#         print("Что то случилось после вызова функции")
#     return wrapper

# def say_hello():
#     print("Hello!")



# # //////////////////////////////
# #? Эти две записи идентичны
# my_decorator(say_hello)()

# @my_decorator
# def say_hello(*, name: str) -> int:
#     print(f"Hello, {name}!")
# # ///////////////////////////////

# say_hello(name="Bodua")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Что то случилось до вызова функции")
        result = func(*args, **kwargs)
        print("Что то случилось после вызова функции")
        return result
    return wrapper

@my_decorator
def add_numbers(*, a: int, b: int)->int:
    print("Adding numbers...")
    return a+b


result = add_numbers(a=3, b=18)
print(result)