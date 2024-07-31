# # import paramiko
# # def ssh_connect(host,username,password,port):
# #     try:
# #         client = paramiko.SSHClient()
# #         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #         client.connect(hostname=,username=username,password=password,port=port)
# #
# #
# #        print("Connection is successful")
# #     except Exception as e:
# #         print(f"Error: {e}")
# # list=["monet","kanth","yadav"]
# # list2=list.copy()
# # print(list2)
# # list=["monet","kanth","yadav"]
# # list2=["monet","kanth","yadav"]
# # list.extend(list2)
# # print(list)
# # list=["monet","kanth","yadav"]
# # list.count()
# # print(list)
# list=["monet","kanth","yadav"]
# print(list[1])
# list.append("golla")
# print(list)
# print(list[2:4])
# list.insert(3,"man")
# print(list)
# list.remove("man")
# print(list)
# list.append("billa")
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.clear()
# print(list)
#
#
# list=["hello","bye"]
# for i in list:
#     print(i)
#     list.append("how")
#     if i == "how":
#         break
#     print(i)
# dict={"name":"mani","age":21,"branch":"info"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(len(dict))
# print(type(dict))
# print(dict["name"])
# dict ["college"] ="mallareddy"
# print(dict)
# dict.update({"age":25})
# print(dict)
# dict.pop("name")
# print(dict)
# dict.popitem()
# print(dict)
# def function(string):
#     count=0
#     for i in string:
#         count+=1
#     return count
# len_string="manikanth"
# len=function(len_string)
# print(len)


# import re
#
# def split(string):
#   pattern = r"\S+"  # Matches one or more non-whitespace characters
#   return re.findall(pattern, string)
#
# # Example usage
# my_string = "This is a sentence to split"
# words = split(my_string)
# print( words)
############fibnacci series
# def fibnacci(n):
#     if n<=0:
#         return [0]
#     elif n==1:
#         return [1]
#     elif n==2:
#         return[0,1]
#     fibnacci_series=[0,1]
#     for i in range(2,n):
#        next=fibnacci_series[-1]+fibnacci_series[-2]
#        fibnacci_series.append(next)
#     return fibnacci_series
# fib=10
# fib2=fibnacci(fib)
# print(fib2)
######################################
# class Book:
#     # print("this is class")
#
#     def display(self):
#         a=20
#         b=30
#
# #         print(a+b)
# obj=Book()
# obj.display()
############################################
# class Addition:
#     def __init__(self,value,values):
#         self.value=value
#         self.values=values
#     def display(self):
#         print(self.value+ self.values)
#         print("____________________")
# for i in range(5):
#     obj=Addition(20,40)
#     obj.display()
#     obj2=Addition(40,60)
#     obj2.display()
#########################################
# class Hello:
#     def __init__(self):
#         print("hello world")
#     def display(self):
#         print("this is Manikanth")
# obj=Hello()
# obj.display()
#######################
# try:
#     a=20
#     print(b)
# except:
#     print(b)
# else:
#     print(a)
# finally:
#     print(b)
########################
#private,protected
class Solution:
    def __init__(self,a,b,c):
     self.__a = a
     self._b = b
     self.c=c
class Nani(Solution):
    def display(self):
        print(self.c)
c=Solution(2 ,7,6)
c.display()









