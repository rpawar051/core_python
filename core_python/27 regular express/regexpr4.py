# regexpr3.py
import re
from traceback import print_tb
matchtab = re.finditer("[^abc]", "stcA#6@Ra7$bZeP&3Qa")
print("-"*50)
for onematch in matchtab:
    print("start index:{}\t end index:{}\t value:{}".format(onematch.start(),onematch.end(),onematch.group()))
else:
    print("-"*50)
    print("for loop end")
    