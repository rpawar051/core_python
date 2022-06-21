#studunpick.py
#this programs reads student record(s) from the file by using un-pickling concept
import pickle
try:
	with open("stud.data","rb") as fp:
		print("-"*50)
		print("\tS t u d e n t   D e t a i l s")
		print("-"*50)
		while(True):
			try:
				studobj=pickle.load(fp)
				for val in studobj:
					print("\t{}".format(val), end=" ")
				print()
			except EOFError:
				print("-"*50)
				break
		print("-"*50)
except FileNotFoundError:
	print("File does not exists")