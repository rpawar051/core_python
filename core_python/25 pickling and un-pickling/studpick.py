#studpick.py
#This program reads student values from KBD and save in file by using pickling concept.
import pickle
with open("stud.data","ab") as fp:
	while(True):
		try:
			print("-"*50)
			print("Enter Student Details:")
			print("-"*50)
			stno=int(input("Enter Student Number:"))
			sname=input("Enter Student Name:")
			marks=float(input("Enter Student Marks:"))
			cname=input("Enter Student College Name:")
			#create an empty list and append
			lst=[]
			lst.append(stno)
			lst.append(sname)
			lst.append(marks)
			lst.append(cname)
			#save the student object data into the file
			pickle.dump(lst,fp)
			print("-"*50)
			print("Student Data Saved Successfully in File:")
			print("-"*50)
			ch=input("\nDo u Want to Insert Another Record(yes/no):")
			if(ch=="no"):
				print("Thanks for this app!")
				break
		except ValueError:
			print("Don't Enter Strs/Alpha-numerical / Special Symbols for Numerics")