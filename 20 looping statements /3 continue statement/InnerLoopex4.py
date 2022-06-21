#InnerLoopex4.py--using while and for loops
i=1
while(i<6):
	print("Outer Loop-->Val of i={}".format(i))
	for j in range(1,3):
		print("\tInner  Loop-->Val of j={}".format(j))
	else:
		print("\n\t Inner loop execution over")
	i=i+1
else:
	print("\n outer loop execution over")
print("\n\n Program completely Executed")
