#globallocalex1.py
def learncrs1():
	sub1="Data Science"  # here sub1 is called Local Variable
	print("in {} Applications, we use {} programming:".format(sub1,proglang))
	#print(sub2,sub3)--invalid, bcoz sub2 and sub3 are local variables of other function

def learncrs2():
	sub2="Artificial  Inteligence"  # here sub2 is called Local Variable
	print("in {} Applications, we use {} programming:".format(sub2,proglang))
	#print(sub1,sub3)--invalid, bcoz sub1 and sub3 are local variables of other function
def learncrs3():
	sub3="Machine-Deep Learning" # here sub3 is called Local Variable
	print("in {} Applications, we use {} programming:".format(sub3,proglang))
	#print(sub1,sub2)--invalid, bcoz sub1 and sub2 are local variables of other function.

#main program
proglang="PYTHON"  # here 'proglang' is called Global Variable
learncrs1()
learncrs2()
learncrs3()