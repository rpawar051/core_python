# d1 = {'k1':'v1','k2':'v2'}
# temp_dict = dict()
# for x, y in d1.items():
#     temp_dict[y] = x

# print(temp_dict)



# from logging import exception


s1 = "my name is aditya"
# # ********
# # *my    *
# # *name  *
# # *is    *
# # *aditya*
# # ********
# # t= "*******"
my_s1 = s1.split(' ')
# higher_length = len(my_s1) +1
# for i in range(0, higher_length+1):
    
#     # for (t, a,b,c,d) in zip(temp.split(' '),my_s1[0],my_s1[1],my_s1[2],my_s1[3]):
#     if (i == 0) or (i == (higher_length-1)):
#         print("* " * higher_length)
#     elif i == len(my_s1):
#         continue
#     # if len(my_s1[i])!= 5:
#     #     c = 5 - len(my_s1[i])
#     #     # print(c)
#     #     for k in range(0, c):
#     #         my_s1[i].join(' ') 
#     try:   
#         print("*", my_s1[i] , "*")
#     except:
#         break
    
s = [len(x) for x in my_s1]
top_length = s[-1]
# print(s[-1])
print("* "* top_length)
for i in range(0, len(my_s1)):
    # new_s = ''
    # for j in range(len(my_s1[i]), top_length):
    #     new_s = my_s1[i] + ' '
    
    print("* ", my_s1[i], " *")

else:
    print("* "* top_length)

    
    