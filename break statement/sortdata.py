#sortdata.py
#accepting number of numerical values and sort then in ASC and DESC order
n=int(input("Enter How many numbers u want to sort:"))
if(n<=0):
	print("{}  is invalid input:".format(n))
else:
	lst=list()   # creating an empty list  
	print("Enter {} Values for list:".format(n))
	for i in range(1,n+1):
		val=int(input())
		lst.append(val)
	else:
		print("Original Elements:{}".format(lst))
		#sort the data in ASC Order
		lst.sort()
		print("Sorted  Elements in ASC Order :{}".format(lst))
		#sort the data in DESC Order
		lst.sort(reverse=True)   #  (or) lst.reverse()
		print("Sorted  Elements in DESC Order :{}".format(lst))