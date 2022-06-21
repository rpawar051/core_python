#reduceex3.py
import functools
print("Enter Values dynamically for finding their sum:")
lst=[float(x) for x in input().split(",")]
result=functools.reduce(lambda a,b: a+b, lst)
print("---------------------------------")
print("Original Values:")
print("---------------------------------")
for val in lst:
	print(val)
print("---------------------------------")
print("Sum={}".format(result))