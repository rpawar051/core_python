#breakex5.py
s="Mississippi"
cnt=0
for i in range(0, len(s)):  # range(0,11)---range(0,11-1
	if (i==4):
		break
	print("{}".format(s[i]), end="")