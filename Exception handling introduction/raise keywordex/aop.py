#aop.py-----File name and treated as module name
from kvr import KvrDivisionError
def  division(a,b):
	if(b==0):  # at this statement when b ==0 then we must raise KvrDivisionError explicitly
		raise KvrDivisionError   
	else:
		c=a/b
		return c
	
#Phase-2: In this phase , we develop programmer-defined function and raising an exception(s)