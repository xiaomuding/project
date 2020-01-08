d = {"a":1,1:"a",2:"b","b":2,'asd':89}

print(type(d))
print(d["b"],d[1])

#判断key是否存在
print('asd' in d)
print(89 in d)
for key in d:
    print(key,d[key])

for key,value in d.items():
    print(key,value)