#readval1.py
print("Enter the Values")
lst=[float (x) for x in input().split(",")  ]   # 100,200,300,400,500,20 read dynamically until we press enter key
print("type of lst=",type(lst))
print(lst)