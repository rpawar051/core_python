#globalvarmodex1.py
a=10
b=20 # here 'a' and 'b' are called Global Variables
def  update1():
	print("In update1()")
	global a,b
	a=a+1
	b=b+1
	print("Val of a(global)={}".format(a)) # 11
	print("Val of b(global)={}".format(b)) # 21
	print("----------------------------------------------")
def update2():
	print("In update2()")
	global a,b
	a=a*10
	b=b*10
	print("Val of a(global)={}".format(a)) # 110
	print("Val of b(global)={}".format(b)) # 210
	print("----------------------------------------------")

#main program
print("Main Program")
print("--------------------------------------------")
print("val of a(gobal)={}".format(a))#10
print("val of b(gobal)={}".format(b))#20
print("--------------------------------------------")
update1()
print("Main Program")
print("--------------------------------------------")
print("val of a(gobal)={}".format(a))#11
print("val of b(gobal)={}".format(b))#21
print("--------------------------------------------")
update2()
print("Main Program")
print("--------------------------------------------")
print("val of a(gobal)={}".format(a))#110
print("val of b(gobal)={}".format(b))#210
print("--------------------------------------------")
