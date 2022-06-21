#simpleifex3.py
#program for accepting any numerical value and decide whether it is +ve or -ve or 0
n=float(input("Enter any numerical Value:"))  # n= 0
if (n>0):
	print("{} is Possitive".format(n))
if(n<0):
	print("{} is Negative".format(n))
if(n==0):
	print("{} is ZERO".format(n))
print("\nprogram finished its execution!")