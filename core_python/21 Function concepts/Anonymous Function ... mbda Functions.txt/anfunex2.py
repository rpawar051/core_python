#program forbiggest of  two number by using Anonymous Function
#anfunex2.py
big=lambda k,v : k if k>v else v


#main program
x1=float(input("Enter First Value:"))
x2=float(input("Enter First Value:"))
res2=big(x1,x2)
print("big({},{})={}".format(x1,x2,res2))

#big=lambda x,y,z: x if x>y and x>z else y if y>z else z