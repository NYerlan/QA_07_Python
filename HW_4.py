# Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
from functools import reduce


# def square(a):
#     peri = a * 4
#     square = a * a
#     diag = (a ** 2) + (a ** 2)
#     my_tuple = (peri, square, diag)
#     print(type(my_tuple))
#     print(my_tuple)
#
# square(3)

# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
# def myDict(**kwargs):
#     return kwargs
# # new_dict = {
# #     "name": "John",
# #     "last_name": "Smith",
# #     "age": "25",
# # }
#
# print(myDict(name="John", last_name="Smith", age =35, position="web developer"))
# print(myDict(name="Anna", last_name="Davis", age=28, position="HR"))
# # print(myDict(new_dict["name"]))
#
# # Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# # создайте новый список, содержащий только
# # положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)

# Используя лямбда выражение, получите результат перемножения значений в предыдущем списке

# print(reduce(lambda x, y: x * y, my_list))

# Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# import time
# def my_decor(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#
#     return wrapper
# @my_decor
# def count():
#     print(10000 ** 5)
#
# count()

# Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.

from my_calc import *
print(sum_it(3, 2))
print(sub_it(5, 4))
print(mult_it(3, 5))
print(div_it(4, 2))
