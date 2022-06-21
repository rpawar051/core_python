#reduceex1.py
import functools
lst=[10,20,34,11,22,67,38,78,45,21]
result=functools.reduce(lambda x,y: x if x>y else y  , lst)
print("Original Values:")
print("---------------------------------")
for val in lst:
	print(val)
print("---------------------------------")
print("Big={}".format(result))