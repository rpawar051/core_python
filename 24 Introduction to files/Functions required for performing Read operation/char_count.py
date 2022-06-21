import collections
import pprint
with open("Functions required for performing Read operation.txt", 'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)
print(count_value)