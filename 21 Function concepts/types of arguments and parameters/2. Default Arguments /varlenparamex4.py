#varlenparamex4.py
def findsum(sname, *n,city="HYD"):
	print("-------------------------------------------")
	print("Student Name:{} and lives in {}".format(sname,city))
	s=0
	for val in n:
		print("\t{}".format(val),end=" ")
		s=s+val
	print()
	print("\tsum={}".format(s))
#main program
findsum("Rossum",10,20)
findsum("KVR",10,20,30)
findsum("Rahul",10,20,30,40)
findsum("Atulya",10,20,30,40,50)
findsum("Ramu",10,20,30,40,50,60)
#findsum("srikar",city="MH",45,6,7)  SyntaxError: positional argument follows keyword argument
findsum("srikar",45,6,7,city="MH")  
#findsum(45,6,7,city="MH",sname="srikar")  TypeError: findsum() got multiple values for argument 'sname'
