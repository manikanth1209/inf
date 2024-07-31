'''''myset={"aple","banana","cherry","cherry"}
for i in myset:
    print(i)
    
myset={"aple","banana","cherry","cherry"}
myset.add("orange")
print(myset)
myset={"aple","banana","cherry","cherr"}
myset2={"curry","carrot"}
myset.update(myset2)
print(myset)
myset={"aple","banana","cherry"}
#myset.discard("banana")
#print(myset)
myset.pop()
print(myset)
myset.clear()
print(myset)
thisset = {"aple","banana","cherry"}
del thisset
print (thisset)
set1 = {"mani","nanai"}
set2 = {1,2,3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set3 = set1 | set2 | set3 | set4
print(set3)'''
set3 = {"John", "Elena","apple"}
set4 = {"apple", "bananas", "cherry"}
set4 =  set3 ^ set4
print(set4)







