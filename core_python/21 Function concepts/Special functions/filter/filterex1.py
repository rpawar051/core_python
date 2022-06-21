#filterex1.py-------filter() with normal functions

def  posfun(n):
	if n>0:
		return True
	else:
		return False

#main program
lst=[12,-34,56,-55,0,-44,12,34,-67]
obj=filter( posfun, lst)
print("type of obj=",type(obj)) # <class 'filter'>
print("values of obj=",obj)
#convert filter oibj into list obj
ps=list(obj)
print("\nPossitive Values=",ps)