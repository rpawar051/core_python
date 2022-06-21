#FileWriteEx1.py
#create a file and write the value 10 and "python" and 44.44
no=20
cname="KVR"
marks=11.11
#choose the file name and open it into write mode
with open("hyd.data","a") as fp:
	fp.write("Roll Number : "+ str(no)+"\n")
	fp.write("Name : "+ cname+"\n")
	fp.write("Marks : " + str(marks)+"\n")
	print("Data Written successfully in write mode:")

