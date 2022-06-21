#continuestex4.py
lst=[10,-20,0,30,-40,-50,60,-70,80]
print("List of Negative Values:")
for val in lst:
	if(val>=0):
		continue 
	else:
		print(val)
