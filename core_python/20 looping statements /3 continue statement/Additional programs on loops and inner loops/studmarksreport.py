#studmarksreport.py
#accept the student details
#Validation of student number----100--200
while(True):
	stno=int(input("Enter Student Number(100-200):"))
	if((stno>=100) and (stno<=200) ):
		break
#accept name
sname=input("Enter the student name:")
#accept and validate C marks
while(True):
	cm=int(input("Enter Marks in C:"))
	if((cm>=0) and (cm<=100) ):
		break
#accept and validate CPP marks
while(True):
	cppm=int(input("Enter Marks in CPP:"))
	if((cppm>=0) and (cppm<=100) ):
		break
#accept and validate PYTHON marks
while(True):
	pym=int(input("Enter Marks in PYTHON:"))
	if((pym>=0) and (pym<=100) ):
		break
#calculate  total marks and Percentage of Marks 
totmarks=cm+cppm+pym
percentmarks=(totmarks/300)*100
#decide the grade cm=90 cpp=100   pym=90
if ((cm<40) or (cppm<40) or (pym<40) ):
	grade="FAIL"
else:
	if( (totmarks>=250) and (totmarks<=300) ):
		grade="DISTINCTION"
	elif((totmarks>=200) and (totmarks<=249)):
		grade="FIRTST"
	elif((totmarks>=150) and (totmarks<=199)):
		grade="SECOND"
	elif((totmarks>=120) and (totmarks<=149)):
		grade="THIRD"
#display the student marks report
print("=====================================================")
print("\tS T U D E N T  M A R K S  R E P O R T")
print("=====================================================")
print("\tStudent Number:{}".format(stno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in CPP:{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pym))
print("----------------------------------------------------")
print("\tStudent Total Marks:{}".format(totmarks))
print("\tStudent Percentage of Marks:{}".format(percentmarks))
print("\tStudent  Result :{}".format(grade))
print("==============================================")


