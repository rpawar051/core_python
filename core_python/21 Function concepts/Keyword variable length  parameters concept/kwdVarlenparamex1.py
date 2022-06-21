#kwdVarlenparamex1.py
def  disp(**a): #here **a is called keyword variable length parameter and whose type is dict
	print("-----------------------------------")
	for k,v in a.items():
		print("{}--->{}:".format(k,v))
	print("-----------------------------------")


#main program
disp(roses="red", violets="blue")
disp(name="Ramu",sub1="Java",sub2="Python")
disp(empno=11,ename="Rossum",sub="Python", hobby="Research")
disp(city="Hyd")