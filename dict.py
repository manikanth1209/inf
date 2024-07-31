'''dict = {
 "name" : "mani",
  "age"  :  21,
 "branch": "inforamtion"
}
dict2=dict.keys()
print(dict2)
dict["cgpa"]=8.2
print(dict2)

dict = {
 "name" : "mani",
  "age"  :  21,
 "branch": "inforamtion"
}
dict2=dict.values()
print(dict2)
dict["cgpa"]=8.2
print(dict2)
dict = {
 "name" : "mani",
  "age"  :  21,
 "branch": "inforamtion"
}
dict2=dict.items()
print(dict2)
dict["cgpa"]=8.2
print(dict2)
dict["age"]=22
print(dict)
dict.pop("cgpa")
print(dict)
dict["year"]=2020
print(dict)
dict.popitem()
print(dict)
print(dict)
dict=list(dict.items())
print(dict)
dict3=dict.copy()
print(dict3)
dictionary = {
  "child1": {
  "name" : "mami"
  },
   "child2":{
   "name":"hari"
  }
}'''
x={"name","name","name"}
y=0
thisdict = dict.fromkeys(x,y)
print(thisdict)
