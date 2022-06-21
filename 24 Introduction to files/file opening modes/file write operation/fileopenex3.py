# fileopenex3.py
try:
    fp = open("kvr2.data", "x")
    print("kvr2.data file opened successfully in exclusively in write Mode:")
except FileExistsError:
    print("File already exists")