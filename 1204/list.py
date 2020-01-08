li = [1,2,3,3,"sdf",[1,2,3],{1:"one",2:"two"}]

print(li[-1])
print(li[1])

print(li.index(3))
print(li.index("sdf"))
print(li.__contains__(1))
li.append("dfg")
li.append([1,2,3])
li.extend([78,69])
print(li)

print(not li)

kong = [None]
print( not kong)

for i in li:
    print(i)
print("**********************")
for i in range(len(li)):
    print(li[i])


t = (1,2,3,4)
li[2] = "sdfsdfgg"
print(li)
print(type(t))


del(li[0])
print(li)