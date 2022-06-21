#globalfunex1.py
a=10
b=20
c=30
d=40 # here 'a','b','c' and 'd' are called global variables.
def operations():
	global c,d
	c=c+1
	d=d+1
	a=100
	b=200  # here 'a' and 'b' are called local variable
	print(a,b,c,d) # 100,200 31,41
	print("---------------------------------------------")
	gvd=globals() # here gvd is a global variable dict object contains all global variable information in the form (key,value)
	x1=gvd['a']    # (or)  globals() ['a']      globals()['b']
	x2=gvd['b']
	print("Val of a (global)={}".format(x1))
	print("Val of b (global)={}".format(x2))
	print("Val of c (global)={}".format(c))
	print("Val of d (global)={}".format(d))
	print("Val of a (local)={}".format(a))
	print("Val of b (local)={}".format(b))


#main program
operations()