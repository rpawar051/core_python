#FileReadEx4.py
#This Program reads all the lines  from the file and dispalys the file data on the console-----readlines()
try:
	fname=input("Enter File Name for reading its content:")
	with open(fname,"r") as fp:
		filedata=fp.readlines()
		for line in filedata:
			print(line,end="")
except FileNotFoundError:
	print("File does not exists")