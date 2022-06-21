#program for finding biggest of three numbers 
#big.py
a=int(input("Enter First Number:"))   # a=10
b=int(input("Enter Second Number:"))#b=20
c=int(input("Enter Third Number:")) #c=30
if ((a==b) and (b==c)):
	print("ALL VALUES ARE EQUAL:")
else:
	big=a;
	if( b>big):
		big=b                   
	if(c>big):
		big=c
	print("Biggest({},{},{})={}".format(a,b,c,big))