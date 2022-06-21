#InnerLoopex7.py
n=int(input("Enter How many Mul tables u want:"))
if(n<=0):                                                                                    
	print("{} is invalid input:".format(n))
else:
	lst=list() # create an empty list
	print("Enter {} Numbers for generating Mul Tables:".format(n))
	for num in range(1,n+1):
		val=int(input())
		lst.append(val)
	else:
		for n in lst:
			if(n<=0):
				print("{} is invalid input:".format(n))
			else:
				print("--------------------------------------------")
				print("\tMul Table for {}".format(n))
				print("--------------------------------------------")
				for i in range(1,11):
					print("\t{} x {} = {}".format(n,i,n*i))
				else:
					print("--------------------------------------------")
