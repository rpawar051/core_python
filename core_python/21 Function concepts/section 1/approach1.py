#approach1.py
def  circlearea(r):
	ac=3.14*r**2
	return ac

#main program

x=float(input("Enter Radius:"))
res=circlearea(x)   # Function call
print("Area of Circle={}".format(res))