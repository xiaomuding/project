import string
#去除空格
a = "  sdf  dfg "
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(a)

#字符串链接
s1 = "sdf"
s2 = "fghf"
print(s1+s2)

#大小写
s = "dgfdgfdg"
print(s.upper())
print(s.upper().lower())
print(s.capitalize())

#位置比较
s1 = "sdfsdfdsg"
s2 = "dfdgfsdsfsdf"
print(s1.index("dsg"))
try:
    print(s2.index("kjhh"))
except ValueError:
    print("not found")
print(s1 == s1)
print(s1 > s2)
print(s1 < s2)

print(len(s1) > len(s2))
print(len(s1) < len(s2))

print(len(""))
print(len("  "))

#分割和链接
s = ", sdf,dfg,,dfg,dfg"
splitted = s.split(",")
print(splitted)
print(type(splitted))

s = """
sdf
dfg

dfg
wer
fdgg
"""
sp = s.split("\n")
sp1 = s.splitlines()
print(sp)
print(sp1)

s = ["ddf","dfg","dfg","dfg"]
print("\t".join(s))
#常用判断
s = "sdgfdgfdg"
print(s.startswith("sdg"))
print(s.endswith("g"))
print("2324sdfs".isalnum())
print("sdfdsf\t".isalnum())
print("sdfds".isalpha())
print("234535".isdigit())
print("   ".isspace())
print("sfsdf".islower())
print("234sdF".islower())
print("2354D".isupper())

print("Wsdf".istitle())


#数字，字符产转化
print(type(str(5.3689)))

print(int("5"))
print(float(5.5689))
print(int("1111",2))

x = None
if x is None:
    print("nome")
else:
    print("not")

str = "4568dfgfd"

for i in str:
    print(i)

for i in range(0,100):
    if i < 10:
        pass
    if i<30:
        continue
    elif i<35:
        print(i)
    else:
        breakpoint()

















