#FileReadEx1.py
#This reads the data from the file and dispalys the file data on the console-----read()
try:
	fname=input("Enter File Name for reading its content:")
	with open(fname,"r") as fp:
		filedata=fp.read()
		print(filedata)
except FileNotFoundError:
	print("File does not exists")