t1 = ("nithya", False, 3.2, 1)
print (t1)
print (t1.index(3.2))
print (tuple(reversed(t1)))
print ("nithya" in t1)
a,b,c,d = t1
print (c)

from copy import deepcopy
t2 = deepcopy(t1)
print (t2)

t3 = ("nithya", "mala", "kamala", "vimala", "mala")
print (''.join(t3))
print (tuple(sorted(t3)))
print (t3[-3])
print (t3.count("mala"))

t4 = t1 + t3
print (t4)