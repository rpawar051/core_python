#filterex3.py--filter() with anonymous functions

findpos=lambda n : n>0
findneg=lambda k: k<0

#main program
lst=[12,-34,56,-55,0,-44,12,34,-67,+53]

ps=list(filter(findpos,lst))
print("\nPosstive Elements={}".format(ps))
print("*"*50)
ns=tuple(filter(findneg,lst))
print("\nNegative Elements={}".format(ns))