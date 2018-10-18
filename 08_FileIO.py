txt = open("./kanchi.txt")
print (txt.read())

txt.seek(0)
print (txt.readline())

for i in txt.readlines():
	if "airport" in i:
		print (i)	

txt = open("./kanchi.txt",'a')
a = input("Enter some interesting things about kanchipuram")
txt.write('\n'+a)
print ("Entered text is added")

txt.close()