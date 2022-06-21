#program for cal sum of two numbers by using approach-4
#sumexample.py
def  addition():
	a=float(input("Enter First Value:"))
	b=float(input("Enter Second Value:"))
	c=a+b
	return a,b,c   # return statement can return either one value or more number of values.

#main program
x,y,z=addition()
print("\n--------------------------------------------------------")
print("First Value={}".format(x))
print("Second Value={}".format(y))
print("Sum of {} and {}={}".format(x,y,z))
print("-----------------------------------------------------------")
print("\n--------------------OR-----------------------------")
k=addition()  # here 'k' is an object of type tuple.
print("Sum ={}".format(k))
print("\nsum of {} and {}={}".format(k[0],k[1],k[2]))
for val in k:
	print("Value:{}".format(val))


"""Note: once a return statement returns multiple values from function definition then we can store those values either by using multi line assignment statement in multiple varaible ( or ) in single variable, which is type tuple.
                         
						 x,y,z=addition()------------multi line assignment statement.
						        (or) 
						  k=addition()  ------------------here 'k' type is tuple"""