#div23.py
# This program accepts two integer values from key board and compute their division
s1=input("Enter First Number:")
s2=input("Enter Second Number:")
#convert s1 and s2 into  int type
try:
	a=int(s1)  
	b=int(s2) 
	c=a/b    
except  ZeroDivisionError as zd:
	print(zd)
except ValueError as ve :
	print(ve)
else:
	print("Val of a={}".format(a))
	print("Val of b={}".format(b))
	print("Division={}".format(c))
finally:
	print("i am fom finally block")