d1 = {1:'One','Name':'Nithya','Age':25,'Qualification':'B.C.A'}
print(d1)
print(d1['Age'])
d1.update({'Place':'Kanchi'})
d1['Name']='Malathi'
del d1['Qualification']
for i,j in d1.items():
    print(i,j)

d2 = {'Tamil':99,'English':94,'Maths':100,'Science':100}
print(sorted(d2.keys()))
print(sorted(d2.values()))
print(sorted(d2.items()))
print(sorted(d2.items(),reverse=True))
print(sum(d2.values()))
print (set(d2.values()))
print(d2.keys() >= d1.keys())

d3 = {'Tamil':80,'English':64,'Maths':98,'Science':77}

from collections import Counter
print(Counter(d2) + Counter(d3))
print(Counter(d3).most_common())

from heapq import nlargest
print(nlargest(2, d3, key=d3.get)) 
from operator import itemgetter
for i, j in nlargest(2, d3.items(), key=itemgetter(1)):
    print(i, j)

l1 = [1,2,3,4,5,6]
l2 = ['Revathi', 'Malini', 'Viyan', 'Shrinitha', 'Sivasankari', 'Meena']
print (dict(zip(l1, l2)))

d4 = {'ddd':'One','Name':'Nithya','Age':'dddd','Qualification':'B.C.A'}
print (map(len,d4.values()))
print (sum(map(len,d4.values())))