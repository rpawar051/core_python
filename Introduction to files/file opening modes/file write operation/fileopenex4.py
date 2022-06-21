# fileopenex4.py
try:
    with open("hyd1.data", "a") as fp:
        print("File opened in read mode successfully")
        print("-"*50)
        print("Type of fp = {}".format(type(fp)))
        print("file opening mode = {}".format(fp.mode)) # r
        print("Can we read ?={}".format ( fp.readable()) ) # True
        print("Can we write ?={}".format ( fp.writable()) ) # False
        print("Line-9->within  with ..open() indentation, is file closed?={}".format(fp.closed )) # False
        print("-"*50)
        
    print("Line-12->out-of  with ..open() indentation, is file closed?={}".format(fp.closed )) # True
except FileNotFoundError: 
	print("File does not exists:")