# class Person:
#   def __init__(self, name, branch):
#     self.name = name
#     self.branch = branch
#   def myfunc(self):
#     print("the name is "+ self.name)
#
# p1 = Person("mani", 23)
# p1.myfunc()
# class Mello:
#   def __init__(self,age,name):
#     self.name=name
#     self.age=age
# p1=Mello("mani",25)
# print(p1.name)
# print(p1.age)

# class Myclass():
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def fun(self):
#     print("my name is",self.name,"age is",self.age)
# class Anotherclass(Myclass):
#   def __init__(self,name,age,role):
#
#       self.role = role
#       self.name = name
#       self.age  = age
#   def fun1(self):
#     print("my name is ",self.name,"and age",self.age,"role is",self.role)
#
# obj1=Anotherclass("mani",24,"developer")
# obj1.fun()
# mod=Anotherclass("mani",24,"developer")
# mod.fun1()
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
##########################################
 ####Single inheritance
# class Parent:
#     def dispaly(self):
#         print("this is parent class")
# class Child(Parent):
#     def display2(self):
#         print("this is child class")
# obj=Child()
# obj.display2()
# obj.dispaly()
########################################
##multilevel Inheritance
# class Parent:
#     def display(self):
#         print("this is parent class")
# class Child(Parent):
#     def display2(self):
#         print("this is child class")
# class Grandchild(Child):
#     def display3(self):
#         print("this is Grandchild")
# obj=Grandchild()
# obj.display3()
# obj.display2()
#############################################
# Hierachical inheritance
# class Parent():
#     def display1(self):
#         print("this is a parent class")
# class Child1(Parent):
#     def display2(self):
#         print("this is child1")
# class Child2(Parent):
#     def display3(self):
#         print("this is child2 ")
# obj=Child2()
# obj.display3()
# # obj.display2()
# obj.display1()
################################################
##multiple Inheritance
# class Father:
#     def display(self):
#         print("this is a father class")
# class Mother:
#     def display2(self):
#         print("this is a mother class")
# class Child(Father,Mother):
#     def display3(self):
#         print("this is a child class")
# obj=Child()
# obj.display3()
# obj.display2()
# obj.display
###################################################
######super keyword
# class Mani:
#     def __init__(self):
#         print("this is mani")
#     def fun1(self):
#         print("this is father class")
# class Money(Mani):
#     def __init__(self):
#         print("this is Money")fas
#         super().__init__()
#
#     def fun2(self):
#         print("this is a mother class")
# obj=Money()
##############################################
###method overloading













