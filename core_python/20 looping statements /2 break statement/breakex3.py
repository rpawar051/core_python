#breakex3.py
s="Mississippi"
cnt=0
for i in range(0, len(s)):  # range(0,11)---range(0,11-1
	if (s[i]=="s"):
		cnt=cnt+1
		print(s[i],end=" ")
		if(cnt==3):
			break
