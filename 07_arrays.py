from array import *
a1 = array('i', [1,3,5,7,9,5,1])
print (a1)
print (a1[0])
print (a1.count(5))
print (a1.itemsize) 
print (a1.buffer_info()) 
print (a1.buffer_info()[1] * a1.itemsize)
for i in a1:
    print (i)

a1.append(11)
print (a1)

l2 = a1.tolist()
print(l2)

a1.insert(12,13)
print (a1)

a1.pop(2)
print (a1)

a1.reverse()
print (a1)

a1.remove(3)
print (a1)

a2 = array('i', [11, 13, 53, 72, 94])
a1.extend(a2)
print (a1)

a3 = array('b', [115, 111, 117, 114, 99, 101])
print (a3.tobytes())

a4 = array('i', [])
l1 = [1, 2, 6, -8]
a4.fromlist(l1)
print(a4)