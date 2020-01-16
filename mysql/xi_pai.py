import random
#for(int i = n - 1; i >= 0 ; i -- )
#    swap(arr[i], arr[rand(0, i)])


list = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    num = random.randint(i,9)
    list[i],list[num] = list[num],list[i]

print(list)

#print(random.randint(1,2))

