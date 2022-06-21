#varlenparamex2.py
def  disp(*a): #here *a is called Variable length Parameter and it can hold Variable														number of vals and whose type is <class,'tuple'>
	print("-----------------------")
	for val in a:
		print(val, end=" ")
	print()

#main program

disp(10) # function call			
disp(10,20)  # function call			
disp(10,20,30)# function call		
disp(10,20,30,40) # function call		
disp(10,20,30,40,50) # function call		
disp("KVR")
disp("KVR","PYTHON")
