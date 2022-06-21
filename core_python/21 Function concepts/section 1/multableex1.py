#multableex1.py
def table(n):
	if(n<=0):
		print("{} is invalid input:".format(n))
	else:
		print("---------------------------------------------")
		print("Mul Table for :{}".format(n))
		print("---------------------------------------------")
		for i in range(1,11):
			print("{} x {} = {}".format(n,i,n*i))
		else:
			print("---------------------------------------------")

#main program
x=int(input("Enter a number:"))
table(x)