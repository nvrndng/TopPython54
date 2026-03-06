# #1
#
# prod = lambda a, b, c: a * b * c
# print(prod(2, 5, 5))


# #2
#
# students = [
#     {"name": "Jennifer", "final": 95},
#     {"name": "David", "final": 92},
#     {"name": "Nikolas", "final": 98},
# ]
#
# # print(type(students))
# # students.sort()
# # print(students)
#
# students.sort(key=lambda i: i["name"])
# print(students)
#
# students.sort(key=lambda i: i["final"], reverse=True)
# print(students)
#
# #3
#
# print(min(students, key=lambda i: i["final"]))
# print(max(students, key=lambda i: i["final"]))


#4

nums = [3, 5, 7, 3, 9, 5, 7, 2]

print(nums)
print(list(map(lambda x: x ** 2, nums)))
print(list(map(lambda x: x ** 3, nums)))