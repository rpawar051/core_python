#multable.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-----------------------------------------------")
	print("Mul Table for :{}".format(n))
	print("-----------------------------------------------")
	i=1
	while(i<=10):
		print("\t{} x {}={}".format(n,i,n*i))
		i=i+1
	else:
		print("-----------------------------------------------")