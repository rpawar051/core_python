#mapex6.py
"""def strop(m,n):
			return (m+"-"+n)"""

strop=lambda m,n:m+"-"+n
#main proigram
lst1=["PYTHON","JAVA","C"]
lst2=["DS","WEB","VLSI"]
lst3=list(map(strop,lst1,lst2))
print("List1\tList2\tList3")
print("-----------------------------")
for v1,v2,v3 in zip(lst1,lst2,lst3):
	print("{}\t{}\t{}".format(v1,v2,v3))
print("-----------------------------")