#mapex4.py
oldsal=[1.2,3.4,4.5,2.3,6.7,1.6]
newsal=list(map(lambda sal:sal+sal*0.1, oldsal))
print("Old Sal list={}".format(oldsal))
print("new Sal list={}".format(newsal))
print("--------------OR-----------------------")
print("Old Sal\tNew Sal")
print("--------------------------------------------")
for ol,nl in zip(oldsal,newsal):
	print("{}\t{}".format(ol,round(nl,2)))
print("--------------------------------------------")