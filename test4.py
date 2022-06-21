l = [9,6,7,8,5,9]
# print(l)
# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]>= l[j]:
#             temp = l[i]
#             l[i] = l[j]
#             l[j] = temp

# print("second higher number is : ", l[-2])

for i in range(0, len(l)-1):
    if l[i] >= l[i+1]:
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp

print(l[-2])
