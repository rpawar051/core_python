#empunpick.py
#This program reads record (s) from a file by using un-pickling concept
import pickle
try:
	with open("emp.data","rb") as fp:
		print("-"*50)
		print("\t\tEmployee Records")
		print("-"*50)
		while True:
			try:
				empobj=pickle.load(fp)
				for val in empobj:
					print("\t{}".format(val), end=" ")
				print()
			except EOFError:
				print("-"*50)
				break
except FileNotFoundError:
	print("File does not exists:")