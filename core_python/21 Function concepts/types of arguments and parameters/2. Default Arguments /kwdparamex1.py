#kwdparamex1.py
def  dispempinfo(eno,ename,cname="IBM"):
	print("{}\t{}\t{}".format(eno,ename,cname))

#main program
print("--------------------------------------------------")
print("Eno\tName\tCname")
print("--------------------------------------------------")
dispempinfo(10,"Rasika")#possitonal Params
dispempinfo(20,"Akhila")#possitonal Params
dispempinfo(ename="hema",eno=30) #keyword arguments
dispempinfo(ename="sonali",eno=40) #keyword arguments
dispempinfo(50,ename="shrusti") #keyword arguments
dispempinfo(60,cname="TCS",ename="Tanima") #keyword arguments
#dispempinfo(cname="TCS",ename="Rasmi", 70) SyntaxError: positional argument follows keyword argument
dispempinfo(cname="TCS",ename="Rasmi", eno=70) #keyword arguments
print("--------------------------------------------------")