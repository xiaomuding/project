import string
print(type(10))
print(type(10.256))
print(type("dsfsf"))
print(type([1,2,3,'a','b']))
print(type((1,2,3,'a','b')))
print(type(set([1,2,3,'a','b'])))
print(type({'a':1,'b':2}))

def func(a,b,c):
    print(a,b,c)
a = func
a(1,2,3)
print(type(a))

print(type(string))

class myclass(object):
    pass

print(type(myclass))

my_class = myclass()
print(type(my_class))

