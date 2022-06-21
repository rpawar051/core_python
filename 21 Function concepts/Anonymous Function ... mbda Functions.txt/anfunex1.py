#program for cal sum of two number with Normal Function and Anonymous Function
#anfunex1.py
def  sumop(a,b):    # Normal Function
	c=a+b
	return c

addop=lambda k,v:k+v  # Anonymous Function Definition


#main program
res1=sumop(10,20)
print("Sum by using Normal Function={}".format(res1))
print("----------------------------------------------------------------------")
x1=float(input("Enter First Value:"))
x2=float(input("Enter First Value:"))
res2=addop(x1,x2)
print("Sum by using  Anonymous  Function={}".format(res2))