# # write 
# l1 = [4,52,98,14,75,36]
# # l1.sort()
# for i in range(0, len(l1)): 
#     for j in range(i, len(l1)): 
#         if l1[i] >= l1[j]:  
#             temp = l1[i]
#             l1[i] = l1[j]
#             l1[j] = temp

# # print(l1)
# print("second largest number : " , l1[-2])

# str = "rahulhimmatraopawar"
# # str_list = str.split('')

# # list = [str[i] for i in range(0, len(str))]
# # print(list)
# dict1 = {i:i.count(i)  for i in str }
# print(dict1) 

# def string_upper(func):
#     def wrapper(a1, a2):
#         s1 = a1.upper()
#         s2 = a2.upper()
#         # return_string = s1.upper() 
#         return s1, s2
#     return wrapper 

# @string_upper
# def display(s3, s4):
#     return "hello", s3, "Good", s4

# print(display("rahul", "morning"))

# def mul(*num):
#     mul = 1
#     print(num)
#     for i in num:
#         mul = mul*i
#         print(i)
#     return mul

# print(mul(1,2,3,5,4,6,9,7,5,10))

# class InterviewbitEmployee:
#     def __init__(self, emp_name):
#         self.emp_name = emp_name
    
#     def introduced(self):
#         print("My name is ", self.emp_name)

# emp1 = InterviewbitEmployee("Mr. Rahul")
# print(emp1.emp_name)
# emp1.introduced()

# # Parent class
# class ParentClass:
#     def par_func(self):
#         print("I am parent class function")
# # Child class
# class ChildClass(ParentClass):
#     def child_func(self):
#         print("I am child class function")

# # Driver code
# obj1 = ChildClass()
# obj1.par_func()
# obj1.child_func()

# # Parent class
# class A:
#     def __init__(self, a_name):
#         self.a_name = a_name
# # Intermediate class
# class B(A):
#     def __init__(self, b_name, a_name):
#         self.b_name = b_name
#         # invoke constructor of class A
#         A.__init__(self, a_name)
# # Child class
# class C(B):
#     def __init__(self,c_name, b_name, a_name):
#         self.c_name = c_name
#         # invoke constructor of class B
#         B.__init__(self, b_name, a_name)
#     def display_names(self):
#         print("A name : ", self.a_name)
#         print("B name : ", self.b_name)
#         print("C name : ", self.c_name)
# # Driver code
# obj1 = C('child', 'intermediate', 'parent')
# print(obj1.a_name)
# obj1.display_names()