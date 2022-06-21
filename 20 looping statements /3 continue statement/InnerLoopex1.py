#InnerLoopex1.py--using inner loops
for i in range(1,6):
	print("Outer Loop-->Val of i={}".format(i))
	for j in range(1,4):
		print("\tInner  Loop-->Val of j={}".format(j))
	else:
		print("\n\t Inner loop execution over")
else:
	print("\n outer loop execution over")
print("\n Program completely Executed")