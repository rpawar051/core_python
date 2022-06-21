#mapex2.py

sqop=lambda n: n**2

#main program
lst=[2,3,4,5,6]
print("Original List={}".format(lst))
print("="*40)
nlst=tuple(map(sqop,lst))
print("Squares List={}".format(nlst))