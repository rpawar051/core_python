#InnerLoopex6.py
lst=[12,13,-4,19,8,9,-12]
for n in lst:
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("-----------------------------------------")
		print("\tMul Table for :{}".format(n))
		print("-----------------------------------------")
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		else:
			print("-----------------------------------------")
