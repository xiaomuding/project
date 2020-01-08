s1 = set([1,1,1,2,2,3,3])

s2 = set([2,3,4,5,6,6])
#print(s1)

print(s1 | s2)
print(s1.union(s2))


print(s1 & s2)
print(s1.intersection(s2))
# 差
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)

#对称
print(s1^s2)
print(s1.symmetric_difference(s2))

s1.update([12,23])
print(s1)