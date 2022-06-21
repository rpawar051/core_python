#totalmarks.py
def  findtotalmarks(sname,cls,cname,**a):
	print("------------------------------------------------------")
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("College Name{}".format(cname))
	if(len(a)==0):
		print("\tNo subjects are there")
	else:
		tot=0
		print("\tSubjects\tMarks")
		print("------------------------------------------------------")
		for k,v in a.items():
			print("\t{}\t\t{}".format(k,v))
			tot=tot+v
		else:
			print("------------------------------------------------------")
			print("\tTotal Marks: {}".format(tot))
			print("------------------------------------------------------")

#main program
findtotalmarks("Rahul","X","SSBT",Eng=60,Hindi=70,Sci=80,Soc=88,Math=99)
findtotalmarks("Ramu","XII",Math=74,Phy=58,Che=55)
findtotalmarks("amar","B.Tech",Cm=40,cpp=50)
findtotalmarks("Rossum","Author")