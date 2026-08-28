#
#!  === === КОРТЕЖИ === ===
#! Структура Tuple используется тогда, когда точно знаю что структуру данных не надо будетменять в будущем

user_roles = ("admin", "editor", "viewer")

# print(user_roles)
# print(len(user_roles))
# for role in user_roles:
#     print(role)
# print("admin" in user_roles)
# print("guest" in user_roles)

# not_tuple = ("admin")
# print(type(not_tuple))
# my_tuple = ("admin",)
# print(type(my_tuple))

role_1, role_2, role_3 = user_roles
print(role_1)
print(role_2)
print(role_3)