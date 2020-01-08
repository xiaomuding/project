def movePanZi(num,source,target,helper):
    if num == 1:
        print(source + "----->" + target)
    else:
        movePanZi(num-1,source,helper,target)
        print(source + "----->" + target)
        movePanZi(num-1,helper,target,source)

movePanZi(3,"A","B","C")

#函数可以作为参数
def sum(x,y,p = None):
    s = x+y
    if p:
        p(s)

sum(100,200)
sum(100,100,print)

#排序
#a = "345435653"
#print(len([5,8,9,4,3,7]))
#print(max(2,3))
'''
def mymax(a,n):
    #lenth = len(a)
    if n == 1:
        return a[0]
    else:
        return max(a[n-1],mymax(a,n-1))

a = [5,8,9,4,3,7]
print(mymax(a,6))
'''





