# #1
# students = [("Иван", 25), ("Мария", 23), ("Петр", 25), ("Анна", 23)]
# dict1 = {}
#
# for name, age in students:
#     if age not in dict1:
#         dict1[age] = []
#     dict1[age].append(name)
#
#
# print(dict1)


# #2
# nums = [1, 1, 1, 2, 2, 3]
# k = 3
# a = {}
#
# for i in nums:
#     if i not in a:
#         a[i] = 1
#     else:
#         a[i] += 1
# b = []
#
# for num, val in a.items():
#     if val >= 2:
#         b.append(num)
#
#
# print(b)



#3

dict1 = {
    1: {"name": "Иван", "age": 17},
    2: {"name": "Максим", "age": 27},
    3: {"name": "Петр", "age": 30},
}

dict2 = {
    2: {"name": "Мария", "age": 20},
    4: {"name": "Анна", "age": 22},
}


dict3 = dict1.copy()
dict3.update(dict2)

# print(dict3)

dict4 = {}

for key, val in dict3.items():
    if val["age"] >= 18:
        dict4[key] = val

print(dict4)
