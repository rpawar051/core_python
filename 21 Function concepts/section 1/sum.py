#sum.py
print("Line:2-->I am there before function defintion:")
def  sumop(k,v):    # here  'k'' 'v' are called Formal parameters
	print("i am at line-4--sumop()")
	r=k+v     # here 'r' is called "Local Variable"
	return r  # here 'return' is statement, which is used for returning the value.

#main program
print("Line:9-->I am there after function defintion:")
result=sumop(10,20) #function call	
print("Line-11--result={}".format(result))
result=sumop(100,200) #function call	
print("Line-13--result={}".format(result))
result=sumop(10.45,120) #function call	
print("Line-15--result={}".format(result))
result=sumop("KVR","PYTHON") #function call	
print("Line-17--result={}".format(result))
#result=addop(10,20)-------error, bcoz addop(), we don't have function call.