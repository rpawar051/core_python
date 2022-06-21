numbers = [2, 3, 5, 7, 11]
output  = [i**2 for i in numbers]
print("List comprehension : ", output)

output_dict = {i:i**2 for i in numbers}
print("Dictionary comprehension : ", output_dict)

