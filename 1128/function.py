def func(a,b):
    print(a,"---",b)
    return a,b
r = func(5,6)
print(r)

def func1(x,y):
    print(x,"+",y)

func1(y=100,x=50)

def myfunction(name,**p):
    print(type(p))
    print(name,"-----",p)

myfunction("saisai",china = "beijing",england = "lodon")

#递归
