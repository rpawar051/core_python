#sortdata1.py
#accepting number of names  and sort then in ASC and DESC order
n=int(input("Enter How many Names u want to sort:"))
if(n<=0):
	print("{}  is invalid input:".format(n))
else:
	lst=list()   # creating an empty list  
	print("Enter {} Names for list:".format(n))
	for i in range(1,n+1):
		val=input()
		lst.append(val)
	print("Original Names:")
	print("------------------------------")
	for names in lst:
		print("\t{}".format(names))
	print("------------------------------")
	#sort the data in ASC Order
	lst.sort()
	print("Sorted  Names in ASC Order")
	print("------------------------------")
	for names in lst:
		print("\t{}".format(names))
	print("------------------------------")
	#sort the data in DESC Order
	lst.sort(reverse=True)   #  (or) lst.reverse()
	print("Sorted  Names in DESC Order :")
	print("------------------------------")
	for names in lst:
		print("\t{}".format(names))
	print("------------------------------")
