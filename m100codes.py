# l=[]
# for i in range(100,200):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))
# import math
# from math import factorial
# x=math.factorial(5)
# print(x,end=',')
###########################
# values=input()
# t=values.split(",")
# l=tuple(t)
# print(t)
# print(l)
###########################
# values=[x for x in input().split(',')]
# values.sort()
# print(values)
# s=input()
# values=[word for word in s.split(',')]
# print(','.join(sorted(list(set(values)))))

# m=input()
# d={"DIGITS":0,"LETTERS":0}
# for c in m:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#          d["LETTERS"]+=1
#     else:
#        pass
# print(d["DIGITS"])
# print(d["LETTERS"])
# num=input("enter the values")
# user=list(map(int, num.split()))
#
# if user[0]==6 and user[-1]==6:
#    print("True")
# else:
#    print("False")

# def printValue(s1,s2):
#     print(int(s1)+int(s2))
#
# printValue("3","4")
#
#
# def printValue(n):
#     print(str(n))
#
# printValue(3)

# def printValue(s1):
#     if s1%2==0:
#         print("even")
#     else:
#         print("odd")
#
# printValue(8)

def printDict():
        d=dict()
        for i in range(1,21):
                d[i]=i**2
        for (k,v) in d.items():
            print(v)
printDict()














