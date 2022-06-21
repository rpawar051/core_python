#filterex4.py--filter() with anonymous functions

#main program
lst=[12,-34,56,-55,0,-44,12,34,-67,+53,200,-123,567]
ps=list(filter( lambda n : n>0,lst) )
print("\nPosstive Elements={}".format(ps))
print("*"*50)
ns=tuple(filter(lambda k: k<0,lst))
print("\nNegative Elements={}".format(ns))