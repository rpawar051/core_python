#swap.py
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
print("--------------------------------------------")
print("Original Value of a:{}".format(a))
print("Original Value of b:{}".format(b))
print("--------------------------------------------")
a,b=b,a    #swapping logic using multi line assignment
print("Swapped Value of a:{}".format(a))
print("Swapped Value of b:{}".format(b))
print("--------------------------------------------")