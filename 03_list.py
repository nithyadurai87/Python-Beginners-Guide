l1 = [15,24,85,49,36,17,52,85,95,320,548,22]
print (l1)
print (l1[0])
print (l1[-1])
print (l1[5:])
print (l1[:5])
print (l1[4:9])
print (l1[-4:])
print (l1[:-4])
print (l1[-7:-4])
print (l1[::2])
print (l1[::-2])

l2 = list(l1)
l2.append(93)
print (l2)
print (sorted(l2))
print (l2[1])
l2.sort()
print (l2)
print (l2[1])
print (max(l2))
from random import shuffle
shuffle(l2)
print (l2)

l3 = ['Revathi', 'Malini', 'Viyan', 'Shrinitha', 'Sivasankari', 'Meena']
print(l3.index('Sivasankari'))
print (''.join(l3))
for i,j in enumerate(l3):
	print (i,j)
print(l1+l3)
for i,j in zip(l1,l3):
	print (i,j)
a,b,c,d,e,f = l3
print (d)
import random
print(random.choice(l3))
import itertools
print(list(itertools.chain(*l3)))
#print(list(itertools.permutations(l3)))











