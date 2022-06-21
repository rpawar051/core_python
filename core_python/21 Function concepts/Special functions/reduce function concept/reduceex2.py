#reduceex2.py
import functools
print("Enter Numerical values:")
lst=[ float(x)  for x in input().split(",") ]

result=functools.reduce(lambda x,y: x if x>y else y  , lst)
print("---------------------------------")
print("Original Values:")
print("---------------------------------")
for val in lst:
	print(val)
print("---------------------------------")
print("Big={}".format(result))