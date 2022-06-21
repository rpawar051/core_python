#Program for accepting a numerical number and deciding whether it is pos or neg or zero.
#posnegzero.py
n=int(input("Enter a number:"))
if(n>0):
	print("{} is Possitive".format(n))
else:
	if(n<0):
		print("{} is negative".format(n))
	else:
		print("{} is Zero".format(n))
	
print("Program Finished!")		
