#defparamex1.py
def dispstudinfo(stno,sname,smarks,subject="PYTHON",cnt="INDIA"):
	print("{}\t{}\t{}\t{}\t{}".format(stno,sname,smarks,subject,cnt))


#main program
print("--------------------------------------------------")
print("stno\tName\tMartks\tSubject\tcountry")
print("--------------------------------------------------")
dispstudinfo(10,"Maddi",34.56) # function Call
dispstudinfo(20,"Sagar",44.56) # function Call
dispstudinfo(30,"Anubhav",64.56) # function Call
dispstudinfo(40,"Sravan",22.22) # function Call
dispstudinfo(50,"Bisjit",22.22,"JAVA") # function Call
dispstudinfo(60,"Srikar",22.22) # function Call
dispstudinfo(70,"Ashraf",22.22,"DS") # function Call
print("--------------------------------------------------")