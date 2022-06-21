#FileWriteEx2.py
#create a file and write the data of list 
tpl=(20,"Gosling",44.56,"Java")
#choose the file name and open it into write mode
with open("rs.data","a") as fp:
	fp.writelines("\n"+str(tpl))
	print("Data Written successfully in write mode:")
