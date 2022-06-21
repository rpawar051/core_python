#FileOpenEx1.py
try:
	fp=open("hyd.data","w")
except FileNotFoundError:													   
	print("File does not exists")
else:
	print("File Opened in Read Mode successfully")
	print("-"*50)
	print("Type of fp={}".format(type(fp))) 
	print("File Opening Mode={}".format (fp.mode)) # a+
	print("Can we read ?={}".format ( fp.readable()) ) # True
	print("Can we write ?={}".format ( fp.writable()) ) # True
	print("is file closed?={}".format(fp.closed ))  # False
	print("-"*50)
finally:
	if fp!=None:
		fp.close()
		print("is file closed in finally block?={}".format(fp.closed ))  # True
