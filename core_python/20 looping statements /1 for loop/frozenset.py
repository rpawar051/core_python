#frozensetdisp.py
print("Elements of frozen set")
print("-----------------------------------")
s1={10,20,"python",23.45,"Hyd"}
fs1=frozenset(s1)
for val in fs1:
	print("\t{}".format(val))
else:
	print("\n-----------------------------------")