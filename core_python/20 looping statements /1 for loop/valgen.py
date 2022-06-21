#program for generating 1 to n numbers
#valgen.py
n=int(input("Enter How many Values u want display:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    for i in range(1,n+1):
        print(i,end=" ")  
    else:
        print("\ni am from else")
    print("\nProgram finished")
    