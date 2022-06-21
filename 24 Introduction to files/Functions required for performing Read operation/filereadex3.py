#FileReadEx3.py
#This Program reads a single  data from the file and dispalys the file data on the console-----readline()
try:
	with open("crs.info","r") as fp:
		filedata=fp.readline()
		print(filedata)
		ind=fp.tell()
		print("Pos of fp=",ind)
		filedata=fp.readline()
		print(filedata)
except FileNotFoundError:
	print("File does not exists")