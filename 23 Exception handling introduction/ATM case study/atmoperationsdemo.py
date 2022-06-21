#atmoperationsdemo.py
from atmmenu import menu
import sys
from bankexcep import DepositError,WithdrawError,InSuffFundError
from bankop import *
while(True):
	try:
		menu()
		ch=int(input("\tEnter Ur Choice:"))
		if(ch==1):
			try:
				deposit()
			except ValueError:
				print("Don't enter strs / alpha-numerics / special symbols for Deposit Operation:")
			except DepositError:
				print("Don't try to deposit  -Ve Values and Zero values:")
		elif(ch==2):
			try:
				withdraw()
			except ValueError:
				print("Don't enter strs / alpha-numerics / special symbols for withdraw Operation:")
			except WithdrawError:
				print("Don't try to withdraw  -Ve Values and Zero values:")
			except InSuffFundError:
				print("U Don't have sufficient Funds--u can't withdraw")
		elif(ch==3):
			balenq()
		elif(ch==4):
			print("Thanks for Using this app!")
			sys.exit()
		else:
			print("Ur Choice of Operation is Wrong--try again:")
	except ValueError:
		print("Don't enter strs / alpha-numerics / special symbols for Choice:")