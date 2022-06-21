#bankop.py----file name and treated as module name
from bankexcep import DepositError,WithdrawError,InSuffFundError
bal=500.00  #min balance---global variable

def  deposit():
	damt=float(input("Enter the Deposit Amount:"))  #implicitly ValueError is raising
	if(damt<=0):
		raise DepositError  #explicitly DespositError is raising
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxx234 Credited with INR:{}".format(damt))
		print("Ur Account Current balance INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter the withdraw amount:")) #implicitly ValueError is raising
	if(wamt<=0):
		raise WithdrawError  #explicitly WithdrawError is raising
	else:
		if((wamt+500)>bal):
			raise InSuffFundError
		else:
			bal=bal-wamt
			print("Ur Account xxxx234 Debited with INR:{}".format(wamt))
			print("Ur Account Current balance INR:{}".format(bal))

def  balenq():
	print("Ur Account Current balance INR:{}".format(bal))

