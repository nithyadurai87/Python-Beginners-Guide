print ("hello world")
print ('hello world')
print ("""
This simple book is meant to get you started in programming.
The title says it is the hard way to learn to write code.
but it is actually not.
""")

print (5+8)
print (5+8 < 1+1) 

print ("Addition of 5 & 8:",5+8)
print ('%d is greater than %d'%(7,5))
print ('%s is daughter of %s'%('Nithya','Duraisamy'))
print ('hello {0}! {1}- {2} lady and {3}'.format('Nithya','Sweet',16,'girl'))

a = input("Enter here:")
print ("The entered number is",a)

a = 1
print (type(a))
b = 1.33
print (type(b))
c = [1,3,4,9]
print (type(c))
d = set([1,3,4,9])
print (type(d))
e = {1:'one', 'two' : 2, 2.3 : 'what', 'biteme' :12}
print (type(e))
f = (1,9,7)
print (type(f))
g = "Kavitha Manoharan"
print (type(g))
from array import *
h = array('i', [1,3,5,7,9])
print (type(h))

w,x,y,z = 0,2,3,2
print (x==y)
print (z<y)
print (y<=x)
print (not y<=x)
print ( (x != y) and (x>y) )
print ( (x == y) or (x==z) )
print (x < 10 and y > 1)
print (bool(w))

for i in range(10): # 'Very lucky day'
    print (i)
    
num1 = 100
num2 = 200
if num1>num2:
    print ("%r is greater than %r" %(num1,num2))
else: #elif:
    print ("%r is greater than %r" %(num2,num1))
    
z=0
while z<5:
	print( 'z = ' + str(z) )
	z += 1 # z = z+1

def nithya():
  l1 = [1,3,4,9]
  print (l1[0])
nithya()

def nithya(l1):
  return (l1[0])
print (nithya([1,3,4,9]))
