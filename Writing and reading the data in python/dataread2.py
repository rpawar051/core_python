#dataread2.py
#Program for reading two values and multiply them
print("Enter Val of a:")
a=input()
print("Enter Val of b:")
b=input()
#c=a*b  invalid
x1=float(a)  # converting str into int   "12"--------float
x2=float(b)  # converting str into int
x3=x1*x2
print("mul of {} and {}={}".format(x1,x2,x3))