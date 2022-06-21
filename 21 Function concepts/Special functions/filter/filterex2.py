#filterex2.py--filter() with normal functions

def  posfun(n):
	if n>0:
		return True
	else:
		return False

def  negfun( k ):
	if k<0:
		return True
	else:
		return False

#main program
lst=[12,-34,56,-55,0,-44,12,34,-67,+53]
ps=tuple(  filter( posfun, lst) )
print("\nPossitive Values=",ps)
print("="*40)
ns=list(filter(negfun,lst))
print("\nNegative  Values=",ns)