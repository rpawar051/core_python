#patdemo.py
n=int(input("Enter how many rows traingled pattern u want:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(" *",end="  ")
		print()