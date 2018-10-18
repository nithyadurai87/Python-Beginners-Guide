s1 = set([0, 1, 2, 3, 4])
print (s1)
print(len(s1))
print(max(s1))
print(min(s1))
for i in s1:
    print(i)
    
s1.add(5)
print (s1)

s1.update([9,11])
print (s1)

s1.pop()
print (s1)

s1.discard(4)
print (s1)

s = s1.copy()
print (s)

s.clear()
print (s)

s2 = set([10, 1, 52, 3, 48])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

s3 = set([1, 3])
print(s3 <= s2)
print(s2 >= s3)

s4 = frozenset([0, 1, 2, 3, 4])
s5 = frozenset([10, 1, 52, 3, 48])
print(s4.isdisjoint(s5))
print(s4.difference(s5))