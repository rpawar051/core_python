#mapex5.py
def addop(m,n):
			return (m+n)

#main proigram
lst1=[10,20,30,40]
lst2=[1,2,3,4]
lst3=list(map(addop,lst1,lst2))
print("List1\tList2\tList3")
print("-----------------------------")
for v1,v2,v3 in zip(lst1,lst2,lst3):
	print("{}\t{}\t{}".format(v1,v2,v3))
print("-----------------------------")