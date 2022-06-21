#mapex7.py
#porogram for demostarting un-equal lengths of Itera ble objects
l1=[10,20,30,40]
l2=[100,200]
l3=[10]
l4=list(map(lambda x,y,z:x+y+z, l1,l2,l3))
print("List1\tList2\tList3\List4")
print("-----------------------------")
for v1,v2,v3,v4 in zip(l1,l2,l3,l4):
	print("{}\t{}\t{}\t{}".format(v1,v2,v3,v4))
print("-----------------------------")