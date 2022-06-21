#InnerLoopex2.py---using while loops
i=1
while(i<6):
	print("Outer Loop-->Val of i={}".format(i))
	j=1
	while(j<4):
		print("\tInner  Loop-->Val of j={}".format(j))
		j=j+1
	else:
		print("\n\t Inner loop execution over")
	i=i+1
else:
	print("\n outer loop execution over")
print("\n\n Program completely Executed")