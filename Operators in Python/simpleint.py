#simpleint.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#cal   si and totamt
si=(p*t*r)/100
totamt=p+si                                             
#display the result
print("----------------------------------------------------------------")
print("\tSimple Interest Calculation")                                             
print("----------------------------------------------------------------")
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\tRate of Interest:{}".format(r))
print("----------------------------------------------------------------")
print("\tSimple Interest in Amount:{}".format(si))
print("\tTotal Amount to Pay:{}".format(totamt))
print("----------------------------------------------------------------")