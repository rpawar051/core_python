#readval2.py
print("Enter the Values")
kvr=( float (x) for x in input().split(",")  )   # 1.2,3.4,5.6,7.8 read dynamically until we press enter key
print("type of kvr=",type(kvr))
tpl=list(kvr)
print(tpl)