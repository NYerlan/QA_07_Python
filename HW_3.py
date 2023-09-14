# # 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
#
# # 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #    - получите сумму всех чисел,
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# # a) Using filter get sum of all integers
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# b)
# list_2 = []
# for i in list_1:
#     if isinstance(i, int):
#         list_2.append(i)
# print(sum(list_2))
# #    - распечатайте все строки, где есть буква 'a'
# list_3 = []
# for i in list_1:
#     if isinstance(i, str) and 'a' in i:
#         list_3.append(i)
# print(list_3)
#
# # 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# lst = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(lst)
# print(my_tuple)
# print(type(my_tuple))
# # my_tuple.append("snake")
# print(my_tuple)

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input("Enter family_1 members (with coma): ")
# family_1_members = family_1.split(", ")
# family_2 = input("Enter family_2 members (with coma): ")
# family_2_members = family_2.split(", ")
# if len(family_1_members) > len(family_2_members):
#     print("Family_1 is bigger")
# elif len(family_1_members) < len(family_2_members):
#     print("Family_2 is bigger")
# else:
#     print("Families are equal")
#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# film = {
#     "title": "Avatar",
#     "director": "James Cameron",
#     "year": "2009",
#     "main_actor": "Sam Worthington",
#     "slogan": "I See You"
# }
# print(film)
# print(film.keys())
# print(film.values())
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list = [1, 2, 3, 4, 5, 3, 2, 1]
# my_set = set(list)
# print(my_set)
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# common = set1.intersection(set2)
# print(common)
# diff_for_Set1 = set1.difference(set2)
# print(diff_for_Set1)
# diff_for_Set2 = set2.difference(set1)
# print(diff_for_Set2)
# is_subset1_of_set2 = set1.issubset(set2)
# is_subset2_of_set1 = set2.issubset(set1)
# print(is_subset1_of_set2)
# print(is_subset2_of_set1)