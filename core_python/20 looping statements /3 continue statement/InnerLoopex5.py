#InnerLoopex5.py
n=int(input("Enter How many Mul tables u want:"))  # n=5--->   1   2    3   4   5
if(n<=0):                                                                                    
	print("{} is invalid input:".format(n))
else:
	for i in range(1,n+1):
		print("-----------------------------------------")
		print("\tMul Table for :{}".format(i))
		print("-----------------------------------------")
		for j in range(1,11):
			print("\t{} x {} = {}".format(i,j,i*j))
		else:
			print("-----------------------------------------")