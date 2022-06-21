#numsum.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-----------------------------------------------")
	print("Sum of numbers within :{}".format(n))
	print("-----------------------------------------------")
	i=1
	s=0
	while(i<=n):
		print("\t{}".format(i))
		s=s+i
		i=i+1
	else:
		print("-----------------------------------------------")
		print("\tSum={}".format(s))
		print("-----------------------------------------------")
