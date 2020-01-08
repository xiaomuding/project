
'''
file1 = open("1.txt")


while True:
    line = file1.readline()
    print(line)
    if not line:
        break
file1.close()

print("------------")
'''
file2 = open("1.txt","r+")

for line in file2:
    print(line)
    file2.write("***"+ "sdf" + "***\n")

file2.close()
