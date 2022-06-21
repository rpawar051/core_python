#numgen.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is Invalid Input:".format(n))
else:
	print("--------------------------------------------------")
	print("Numbers within:{}".format(n))
	print("--------------------------------------------------")
	i=1   # initlization part
	while(i<=n):  # cond part
		print("\t{}".format(i))
		i=i+1  #updation part
	else:
		print("--------------------------------------------------")
	print("i am from other statements in program")