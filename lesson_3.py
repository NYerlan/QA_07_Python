
# LIST:

# lst = [10, "Hello", None, True, 25, 34.5]
# print(lst[4])
# print(id(lst))
# print(len(lst))
# print(lst.index(True))
# text = "Bye"
# lst.append(text)
# print(lst)
# lst[-2] = 100.3
# print(lst)
# lst.reverse()
# print(lst)
# print(id(lst))

# lst2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
# print(lst2)
# print(sum(lst2))
# print(min(lst2))
# print(max(lst2))

# lst3 = [1, 2, 3, 4, 5, 6]
# new_lst = []
# for num in lst3:
#     if num % 2 == 0:
#         new_lst.append(num * num)
# print(new_lst)
# lst5 = [5, ["a", "b", "c"], 10]
# print(lst5[1][1])

# List Comprehension:
# new_lst2 = [i * i for i in lst3 if i % 2 == 0]
# print(new_lst2)
# print(len(new_lst2))
# lst4 = [3, 1, 5, 2, 7, 6]
# print(lst4.sort())
# lst4.sort()
# print(lst4)
# print(id(lst4))
# print(type(lst4.sort()))

# TUPLE:
# my_tuple =1, 2, 3
# print(type(my_tuple))
my_tuple2 = ("lemon", "mango", "apple", "cherry", 10, True, 24.5)
print(type(my_tuple2))
# my_tuple3 = ("orange",)
# print(type(my_tuple3))
# lst = list(my_tuple2)
# lst[0] = "orange"
# my_tuple2 = tuple(lst)
# print(my_tuple2)
#
# def sum_it(*args):
#     return sum(args)
# print(sum_it(2, 5, 8, 25))
# print(sum_it(2, 5, 8, 25, 2, 5, 8, 25))

# DICTIONARY:
# my_dict = {
#     "name": "Anna",
#     "age": 30,
#     "department": "IT"
# }
# my_dict2 = {
#     "name": "Alex",
#     "last_name": "Smith",
#     "age": 25,
#     "department": "DEV"
# }
# print(my_dict2)
# print(my_dict2["name"])
# print(my_dict2["department"])
# my_dict2["department"] = "Sales"
# print(my_dict2["department"])
# print(len(my_dict2))
# print(my_dict2.keys())
# print(my_dict2.values())
# print(my_dict2.items())
# print(my_dict2.get("age", "Not found"))
# my_dict2["salary"] = 5000
# print(my_dict2)



# def keywords(**kwargs):
#     return kwargs
#
# print(keywords(name="Alice", last_name="Johns"))

# SETS:
# my_set = {1, 2,  5, 8, 10, 12, 10, 2}
# print(my_set)
# my_list = [1, 2,  5, 8, 10, 12, 10, 2]
# print(my_list)
# my_list2 = list(set(my_list))
# print(my_list2)

# set1 = {1, 2, 3, "one", "ten"}
# set2 = {1, 2, 3, "one", "ten", 100 , 525}
# set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# set1.remove(1)
# print(set1)
# set1.add(8)
# print(set1)
# #
# fs = frozenset({1, 2, 3})
# print(fs[1])
# print(fs)
# fs.remove(1)
# print(fs)
#
# fs.add(4)
# print(fs)

