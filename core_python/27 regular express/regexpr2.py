#regexpr2.py
#This program finds the number of occurences of a word "python" and find the indexes where they present .
# case sensitive  word match for these code.
import re
sp="Python"
givendata="Python is one of functional Prog lang. Python is one the oop lang."
matchtab	=re.finditer(sp,givendata)
noc=0
print("-"*50)
for onematch in matchtab:
	print("start index:{}\t end Index: {}\t value:{}".format(onematch.start(),onematch.end(), onematch.group()))
	noc=noc+1
else:
	print("-"*50)
	print("Number of occurences of '{}'={}".format(sp,noc))
	print("-"*50)