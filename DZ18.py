# #1
#
# str = input("Введите строку: ")
#
# letter1 = str.find("h")
# letter2 = str.rfind("h")
#
# res = str[:letter1] + str[letter2 + 1:]
# print(res)


# #2
#
# str = input("Введите строку: ")
#
# letter1 = str.find("h")
# letter2 = str.rfind("h")
#
# a = str[letter1 +1:letter2]
# revers = a[::-1]
#
# res = str[:letter1 +1] + revers + str[letter2:]
# print(res)


# #3
#
# str = input("Строка: ")
# last = input("Ее заменяемая подстрока: ")
# new = input("На что заменить: ")
# res = ""
# i = 0
#
# while i < len(str):
#     if str[i:i+len(last)] == last:
#         res += new
#         i = i + len(last)
#     else:
#         res += str[i]
#         i += 1
#
# print(res)


#4

str = "Ежевику для ежат\nПринесли два ежа.\nЕжевику еле-еле\nЕжата возле ели съели."
print(str)

a = str.split()
b = 0

for i in a:
    if i[0] == "е" or i[0] == "Е":
        b += 1

print("Количество слов: ", b)