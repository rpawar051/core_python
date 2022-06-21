#program for cal simple interest
#simpleint.py-------->File Name-->and it is treated as Module Name
def  calsimpleint():
	p=float(input("Enter principle Amount:"))
	t=float(input("Enter Time:"))
	r=float(input("Enter Rate of Interest:"))
	si=(p*t*r)/100
	print("-"*50)
	print("Simple Interest Result:")
	print("-"*50)
	print("Principle Amount:{}".format(p))
	print("Time:{}".format(t))
	print("Rate of Interest:{}".format(r))
	print("Simple Interest on Amount:{}".format(si))
	print("-"*50)