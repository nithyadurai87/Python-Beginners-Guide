str1 = "Nithya Duraisamy"
print (str1)
print (str1.replace(" ","-"))
print (str1.split("a"))
print (str1.rsplit('a', 1))
print (str1.count('a'))
print (str1.upper())
print (str1.lower())
print (str1+" Shanmugam")
print (str1*4)
print ('-'.join(str1))
print (reversed(str1))
print (''.join(reversed(str1)))
print (sorted(str1))
print (''.join(sorted(str1)))
print(str1.startswith("nit"))
print (str1[0])
print (str1[0].isdigit())
print (str1.find('u'))
for i,j in enumerate(str1):
	print (i,j)

str2 = "******Nithya Duraisamy********"
print (str.strip("*"))
print (str.rstrip("*"))
print (str.lstrip("*"))

str3 = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
import textwrap
print(textwrap.fill(str3, width=50))
print(textwrap.dedent(str3))
print(textwrap.indent(str3, '> '))  
print (str3.title())

x = 16
print("{:0>3d}".format(x));
print("{:*<5d}".format(x));
print("Alignments:"+"{:<10d}".format(x));
print("Alignments:"+"{:^10d}".format(x));
print("Alignments:"+"{:10d}".format(x));

y = 1524789.5276
print("{:.2f}".format(y));
print("{:+.2f}".format(y));
print("{:.0f}".format(y));
print("{:.2%}".format(y));
print("{:,}".format(y));

z = "32.054,23"
print(z.translate(z.maketrans(',.', '.,')))

