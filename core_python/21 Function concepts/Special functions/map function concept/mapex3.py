#mapex3.py
lst=[2,3,4,5,6,-9]
print("Original List={}".format(lst))
print("="*40)
nlst=tuple(map(lambda n: n**2,lst))
print("Squares List={}".format(nlst))