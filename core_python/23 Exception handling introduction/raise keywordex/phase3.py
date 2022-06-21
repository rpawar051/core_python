#phase3.py
from phase2 import table
from phase1 import InvalidInputError,LoginError
from loginprocess import loginop
try:
	un=input("Enter Ur User Name:")
	pw=input("Enter Ur Password:")
	loginop(un,pw)
except LoginError:
	print("Ur User name (or) password is wrong")
except ValueError:
	print("Don't enter strs / alpha-numerical values / special symbols:")
except InvalidInputError:
	print("Don't enter -ve / zero  Value :")

