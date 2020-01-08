def sum(a):
    if a<0 :
        raise ValueError
    elif a<=1 :
        return a
    else:
        return a + sum(a-1)

print(sum(100))

#f(n) = f(n-1) + f(n-2)

def fn(a):
    if a<1 :
        raise ValueError
    elif a<=2 :
        return 1
    else:
        return fn(a-1) + fn(a-2)

print(fn(30))