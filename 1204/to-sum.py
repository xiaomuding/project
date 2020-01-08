for i in range(2,6):
    print(i)
for i in range(6):
    print(i)

def two_sum(list,sum):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if (list[i] + list[j]) == sum :
                return i,j
    return-1,-1

print(two_sum([1,4,5,8,],9))
print(two_sum([1,4,5,8,],19))
