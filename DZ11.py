#1

# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = input("s = ")
#
# if s == "":
#     print("Ошибка!")
# else:
#     if s in a:
#         print("Yes")
#     else:
#         print("No")


#2

# sybm = input("Введите по порядку, без пробелов, элементы кортежа: ")
#
# if not sybm.isdigit():
#     print("Введите числа!")
# else:
#     a = tuple(sybm)
#     print(a)
#
# b = set(a)
# print(b)
#
# for i in b:
#     print("Количество", i, "=", a.count(i))


# #3
import random
winning_numbers = {random.randint(1, 100) for x in range(5)}
print(winning_numbers)

num = int(input("Введите одно число: "))

if num in winning_numbers:
    print("Поздравляю, вы угадали!")
else:
    print("Попробуйте еще раз")
