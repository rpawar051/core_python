#MultipleLines.py
#This program writes multiple lines of text to the file.
with open("hyderabad.info","a") as wp:
	print("Enter Multiple Lines of text and press('quit') to stop:\n")
	while True:
		mldata=input()
		if(mldata!='quit'):
			wp.write(mldata+"\n")
		else:
			break
	print("\nData written to the file--verify")