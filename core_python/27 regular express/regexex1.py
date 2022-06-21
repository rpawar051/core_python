#regexpr1.py
#This program finds the number of occurences of a word "python" and find the indexes where they present .
import re
sp="Python"
givendata="Python is one of functional Prog lang. Python is one the oop lang."
matchtab	=re.finditer(sp,givendata)
print("type of matchtab obj=",type(matchtab)) 
# type of matchtab obj= <class 'callable_iterator'> 
for onematch in matchtab:
	print("-"*50)
	print("start index: ",onematch.start())
	print("end index: ",onematch.end())
	print("value :",onematch.group())
	print("-"*50)