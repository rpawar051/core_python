#continuestex1.py
lst=[10,20,30,40,50,60,70,80]
for val in lst:
	if (val==30) or (val==70):
		continue
	else:
		print(val)