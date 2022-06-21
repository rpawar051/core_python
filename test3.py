# from operator import le


# string = "salkdfjksgsifuirfuieruiueriuriyuniyrieryuiyivyeiguyaiynief"
# list1 = list()
# slist = list()
# for i in range(0, len(string)):
#     slist.append(string[i])
#     # list1.append(string.count(string[i]))

# dict1 = dict()
# s = list(set(slist))
# for i in range(0, len(s)):
#     # print(s[i], " : ",  string.count(s[i]))
#     list1.append(string.count(s[i]))
#     dict1[s[i]]=string.count(s[i])

# list2 = list1.sort()
# new_list = list()
# dict2 = dict()
# print(list2)
# for i in range(0, len(list1)):
#     new_list.append((s[i],list1[i]))
#     dict2[s[i]]=string.count(s[i])


# # print(list1)
# #print(dict1)
# print(dict2)

string = "grass is greener on the other side";  
freq = [None] * len(string);  
minChar = string[0];  
maxChar = string[0];  
   
#Count each word in given string and store in array freq  
for i in range(0, len(string)):  
    freq[i] = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' ' and string[i] != '0'):  
            freq[i] = freq[i] + 1;  
              
            #Set string[j] to 0 to avoid printing visited character  
            string = string[ : j] + '0' + string[j+1: ];  
              
#Determine minimum and maximum occurring characters  
min = max = freq[0];  
for i in range(0, len(freq)):  
      
    #If min is greater than frequency of a character  
    #then, store frequency in min and corresponding character in minChar  
    if(min > freq[i] and freq[i] != '0'):  
        min = freq[i];  
        minChar = string[i];  
    #If max is less than frequency of a character   
    #then, store frequency in max and corresponding character in maxChar  
    if(max < freq[i]):  
        max = freq[i];  
        maxChar = string[i];  
   
print("Minimum occurring character: " + minChar);  
