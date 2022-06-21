#mapex1.py
def squares(n):
	return (n**2)

#main program
lst=[2,3,4,5,6]
print("Original List={}".format(lst))
print("="*40)
obj=map(squares, lst)  # obj is of type <class,'map'>
nlst=list(obj)
print("Squares List={}".format(nlst))