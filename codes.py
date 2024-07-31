##reverse a string in function
#

# def reverse_function(s):
#
#     return s [::-1]
# value =(input())
# print(reverse_function(value))



# def word_palindrome(s):
#     return s==s[::-1]
# word=input()
# print(word_palindrome(word))


###sum of a number

# def list_function(lst):
#     return sum(lst)
# input_user=input("enter the values by spaces:")
# numbers=list(map(int, input_user.split()))
# print(list_function(numbers))

## max of list
# def max_list(lst):
#     return max(lst)
# user_input=input("enter the values sepearted by spaces:")
# valuse=list(map(int,user_input.split()))
# print(max_list(valuse))

##count vowels in aString
# def my_function(s):
#     vowels="aeiouAEIOU"
#     return sum(1 for char in s if char in vowels )
# values=input()
# print(my_function(values))

### remove duplicates from a string
# def remove_duplicates(lst):
#     return list(set(lst))
# value=input("enter the value by spaces:")
# numbers=list(map(int,value.split()))
# print(remove_duplicates(numbers))

### merge the list
# def function(list1,list2):
#     return list1+list2
# user_input=input("the values")
# user_input2=input("the values")
# list1=list(map(int,user_input.split()))
# list2=list(map(int,user_input2.split()))
# print(function(list1,list2))

## sorting in ascending order
# def my_sort(lst):
#    return sorted(lst)
# user_input=input("enter the values by spaces:")
# numbers=list(map(int,user_input.split()))
# print(my_sort(numbers))


##anagram
# def functtion_anagram(s1,s2):
#     return sorted(s1)==sorted(s2)
# s1=input()
# s2=input()
# print(functtion_anagram(s1,s2))

#
# l=[]
# for i in range(1200,1900):
#     if i%7==0 and i%5!=0:
#         print(i,end=',')


# #
# import math
# print(math.sqrt(8))

# finding the maximum of two numbers
# def function(lst):
#    return max(lst)
# mani=input()
# user=list(map(int,mani.split()))
# print(function(user))

## multiplying
#
# for i in range(1,10):
#     i=i*i
#
# print(i)
# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print(d)

###splitting the values

# user_input=int(input())
# values=list(map(int,user.split(",")))
# print(values)

##upper case and lowercase
# s=input()
# d={"UPPER CASE":0,"LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#          d["LOWER CASE"]+=1
#     else:
#         pass
# print(d["UPPER CASE"])
# print(d["LOWER CASE"])


# def a_bigger(a, b):
#   if a > b and (a - b) >= 2:
#     return True
#   else:
#     return False
#
# s='Hello'
# for char in s:
#     print(char)
# s = 'Hello'
# result = ''
# for ch in s:  ## looping in this way, ch will b
#   result = result +

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def __repr__(self):
#         return f"Point({self.x},{self.y})"
# e = Point(2,4 )
# print(e)
class Employee:
    def __init__(self,string):
         self.string=string
    def __setitem__(self,key,value):
        self.string[key]=value
e =Employee([1,2,3,4])
print(e.string)
e[1]=5
print(e.string)
































