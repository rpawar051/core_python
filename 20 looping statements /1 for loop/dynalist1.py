#program for reading elements in list dynbamically and display the elements of list
#dynalist1.py

n=int(input("Enter How Many elements u want place in list:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=[]   # creating an empty list    (or) lst=list()
	for i in range(1,n+1):
		val=input("Enter {} Value:".format(i))
		lst.append(val)
	else:
		#display the elements of list
		print("---------------------------------")
		print("Elements of List:")
		print("---------------------------------")
		for val in lst:
			print("\t{}".format(val))
		else:
			print("---------------------------------")