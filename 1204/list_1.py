li = list(range(10))
print(li)

print(li[8:9])
print(li[8:])
print(li[0:5:3])

print(li[3:-3])
print(li[9:0:-5])
print(li[::-1])

li = [(i * 2 -1) for i in range(1,10)]
print(li)
li3d = [[0]*3 for i in range(3)]
print(li3d)