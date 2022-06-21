#emppick.py----Program--A
#this program saves the employee details in a file by using pickling  concept
import pickle
with open("emp.data", "ab") as fp:
	noe=int(input("Enter How many Employee u have:"))
	for i in range(1,noe+1):
		print("-"*50)
		print("Enter {}  Employee Details:".format(i))
		print("-"*50)
		eno=int(input("Enter Employee Number:"))
		ename=input("Enter Employee Name:")
		sal=float(input("Enter Employee Salary:"))
		dsg=input("Enter Employee Designation:")
		#create an empty list and  append employee details to the list
		lst=list()
		lst.append(eno)
		lst.append(ename)
		lst.append(sal)
		lst.append(dsg) # lst=[--------------------------]
		#save (or) write lst object into the file
		pickle.dump(lst,fp)
		print("-"*50)
		print("{} Employee Data Saved Successfully in File:".format(i)) 



