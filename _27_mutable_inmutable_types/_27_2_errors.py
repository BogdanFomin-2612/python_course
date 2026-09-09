#
#? РАБОТАЕТ НЕ ВСЕГДА, НАПРИМЕР КОГДА В ЗНАЧЕНИЯХ У КЛЮЧЕЙ ЛЕЖАТ MUTABLE ОБЬЕКТЫ 

# my_dict = {"x": 1, "y": 2}

# another_dict = my_dict.copy()
# another_dict["x"] = 100

# print(my_dict)
# print(another_dict)

# //////////////////////////////
#? НАПРИМЕР ТУТ НЕПРАВИЛЬНО РАБОТАЕТ

# patient_data = {"heart_rate": [60, 61, 63, 60, 61]}

# patient_data_copy = patient_data.copy()
# patient_data_copy["heart_rate"].append(63)

# print(patient_data)
# print(patient_data_copy)

# ///////////////////////////////////
#? А ТУТ ПРАВИЛЬНО

# from copy import deepcopy

# patient_data = {"heart_rate": [60, 61, 63, 60, 61]}

# patient_data_copy = deepcopy(patient_data)
# patient_data_copy["heart_rate"].append(63)

# print(patient_data)
# print(patient_data_copy)

# ///////////////////////////////////
#? НЕПРАВИЛЬНО

# def func_with_computations(*, lst: list[int]) -> None:
#     # some computations
#     lst.clear()

# my_list = [1, 2]

# func_with_computations(lst=my_list)

# print(my_list)

#? ПРАВИЛЬНО

from copy import deepcopy

def func_with_computations(*, lst: list[int]) -> list[int]:
    # some computations
    lst.clear()
    return lst

my_list = [1, 2]

my_list = func_with_computations(lst=my_list)

print(my_list)