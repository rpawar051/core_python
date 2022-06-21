#FileCopy.py
#This program copy the content of one file into another file.
sfile=input("Enter the  Source file name:")
try:
	with open(sfile,"r") as rp:
		dfile=input("Enter the  Destination file name:")
		with open(dfile,"a") as wp:
			#read the data from the file
			filedata=rp.read()
			#write the data to the file
			wp.write(filedata+"\n")
			print("\nSource File Data Copied into Destination File:")

except FileNotFoundError:
	print("File does not exists")