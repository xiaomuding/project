def revert(list,start,end):
    while (start < end) and start<len(list) and end<len(list) :
        list[start],list[end]= list[end],list[start]
        start += 1
        end -= 1


sentence = " how are you , fine, i thanks"

list_or = list(sentence)
#print(list_or)
i = 0
#for i in range(len(list_or)):
while i < len(list_or):
    if list_or[i] != ' ':
        start = i
        end = start
        while ((end)<len(list_or)):
            if list_or[end] != ' ':
                end += 1
                print("***", end)
            else:
                print("break")
                break

        revert(list_or,start,end-1)
        i = end
    else:
        i = i+1

print(list_or)
list_or.reverse()
print(list_or)

print("---"+"".join(list_or)+"----")


