#objsdisp.py
def dispvalues(obj):
	print("-------------------------------------")
	print("Type of obj={}".format(type(obj)))
	print("-------------------------------------")
	for val in obj:
		print("\t{}".format(val))
	else:
		print("-------------------------------------")

def dispdictvalues(obj):
	print("-------------------------------------")
	print("Type of obj={}".format(type(obj)))
	print("-------------------------------------")
	for k,v in obj.items():
		print("\t{}-->{}".format(k,v))
	else:
		print("-------------------------------------")
#main program
lst=[10,"KVR",11.11,"Hyd"]
dispvalues(lst)
tpl=(10,20,-30,"python")
dispvalues(tpl)
stv={10,20,30,40,True}
dispvalues(stv)
d={10:"apple",20:"mango",30:"kiwi"}
dispdictvalues(d)