#aopdemo.py
from aop import division
from kvr import KvrDivisionError
try:
	a=float(input("Enter First Value:"))
	b=float(input("Enter Second Value:"))
	result=division(a,b) # calling the function and raised an exception
except KvrDivisionError:
	print("Don't enter zero for den....")
except ValueError:
	print("Don't enter Strs/ alpha-numerics / special symbols:")
else:
	print("Division={}".format(result))
finally:
	print("i am from finally block")

#Phase-3: In this phase , we  are handling the raised exceptions.
