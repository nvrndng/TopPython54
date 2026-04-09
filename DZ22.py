# #1
#
# with open("text1.txt","r") as f:
#     line = f.readlines()
#
# pos1 = 1
# pos2 = 2
#
# line[pos1], line[pos2] = line[pos2], line[pos1]
# with open("text1.txt","w") as f:
#     for i in line:
#         f.write(i.strip() +"\n")
#

# #2
#
# with open("text1.txt","r") as f:
#     line = f.readlines()
#
# line.reverse()
# with open("text1.txt","w") as f:
#     f.writelines(line)
#

#3
with open("firstfile.txt") as f, open("secondfile.txt") as t, open("thirdfile.txt", "w") as m:
    m.write(f.read())
    m.write(t.read())