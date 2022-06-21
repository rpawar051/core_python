import collections
import pprint

s = "rahulhimmatraopawar"
data_count = collections.Counter(s)
print(dict(data_count))
count_value = pprint.pformat(data_count)

print(count_value)