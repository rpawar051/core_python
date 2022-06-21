#varlenparamex3.py
def  disp(*a,city="HYD"): #here *a is called Variable length Parameter and it can hold Variable														number of vals and whose type is <class,'tuple'>
	print("-----------------------")
	print("My City:{}".format(city))
	for val in a:
		print(val, end=" ")
	print()

#main program

disp(10) # function call			
disp(10,20)  # function call			
disp(10,20,30)# function call		
disp(10,20,30,40) # function call		
disp(10,20,30,40,50) # function call		
disp("KVR")# function call	
disp("KVR","PYTHON") # function call	
print("=========================")
disp("Bisjit","PYTHON",city="MH") #valid
#disp(city="MH","Bisjit","PYTHON")  SyntaxError: positional argument follows keyword argument
