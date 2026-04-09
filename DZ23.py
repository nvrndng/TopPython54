import os

# os.makedirs("Work/F1")
# os.makedirs("Work/F2/F21")
# ff = open("Work/w.txt", "w")
# ff.close()
# f1 = open("Work/F1/f11.txt", "w")
# f1.close()
# f2 = open("Work/F1/f12.txt", "w")
# f2.close()
# f3 = open("Work/F1/f13.txt", "w")
# f3.close()
# f4 = open("Work/F2/F21/f211.txt", "w")
# f4.close()
# f5 = open("Work/F2/F21/f212.txt", "w")
# f5.close()
#
# with open("Work/w.txt", "w") as f:
#     f.write("Hello World")
#
# with open("Work/F1/f12.txt", "w") as f:
#     f.write("Lorem ipsum dolor sit amet")
#
# with open("Work/F2/F21/f211.txt", "w") as f:
#     f.write("Let's repeat lorem ipsum dolor sit amet")
#
# with open("Work/F2/F21/f212.txt", "w") as f:
#     f.write("Сегодня отличный солнечный день")


print("Обход Work снизу вверх:")
for root, dirs, files in os.walk("Work", topdown=False):
    print(root)
    print("\t", dirs)
    print("\t\t", files)

print(" ")
print("-"*30)
print(" ")

for root, dirs, files in os.walk("Work"):
    print(root)
    print("\t", dirs)
    print("\t\t", files)