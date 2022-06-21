#loginprocess.py
from phase1 import LoginError
from phase2 import table
def loginop(un,pw):
	if(un=="kvr") and (pw=="python"):
		table()
	else:
		raise LoginError