#posparamex1.py
def dispstudinfo(stno,sname,smarks):
	print("{}\t{}\t{}".format(stno,sname,smarks))


#main program
print("--------------------------------------------------")
print("stno\tName\tMartks")
print("--------------------------------------------------")
dispstudinfo(10,"Rossum",34.56) # function Call
dispstudinfo(20,"Gosling",44.56) # function Call
dispstudinfo(30,"Ritche",64.56) # function Call
dispstudinfo(40,"Trump",22.22) # function Call
print("--------------------------------------------------")