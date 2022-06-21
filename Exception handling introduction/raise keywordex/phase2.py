#phase2.py---file name and treated as Module Name
from phase1 import InvalidInputError
def    table():
	n=int(input("Enter a number:"))  # implicitly PVM raise ValueError
	if (n<=0):
		raise InvalidInputError   # hitting the programmer-defined exception
	else:
		print("-"*50)
		print("Mul Table for :{}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		else:
			print("-"*50)
