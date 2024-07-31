'''list=["fryits","banana"]
for i in list:
    print(i)
#looping through a string
string="manikanth"
for i in string[2:8]:
    print(i)
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i=="banana":
        continue
    print(i)
for i in range(8,81,8):
    print(i)
else:
    print("finally executed")
for i in range(35):
    if i==25:
        continue
    print(i)
else:
    print("finally executed")'''
# for i in range(1,6):
#     for j in range(6):
#         print(i,j)
num=3
# for i in range(2,num):
#     if num % i == 0:
#         print("it is not  prime")
#         break
#     else:
#         print("it is  prime")
b=int(input())
e=int(input())
for num in range(b,e):
    if num>1:
       for i in range(2,num):
           if num%i==0:
               break
       else:
           print(num)

