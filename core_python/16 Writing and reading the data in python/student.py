#student.py
#reading student details from KBD
sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
marks=float(input("Enter Student marks:"))
cname=input("Enter Student College Name:")
#display the student details
print("\n====================================")
print("S t u d e n t   D e t a i l s")
print("====================================")
print("Student Number:{}".format(sno))
print("Student Name:{}".format(sname))
print("Student Marks:{}".format(marks))
print("Student College Name:{}".format(cname))
print("====================================")