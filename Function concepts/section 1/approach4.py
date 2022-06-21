#approach4.py
def  area():
	r=float(input("Enter Radius:")) #taking input inside of function body
	ac=3.14*r**2   #processing inside of function body
	return ac       #giving result to the function call.

#main program
res=area()
print("Area of Circle={}".format(res))