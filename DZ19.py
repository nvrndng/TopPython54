import re

s = input("Введите адреса электронной почты: ")

reg = r"[\w.-]+@[\w.-]+\.\w+"


print(re.findall(reg, s))