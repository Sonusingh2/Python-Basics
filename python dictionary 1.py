#1 dictionary Intro
'''dict={"name":"sonu",
      "score":9.6,
      "marks":[1,2,3,4,5]}
print(dict)   
dict["score"]=10
print(dict)

#2 Null dictionary
null={}
null["name"]="sonu"
print(null)

#3 Nested Dictionary
dict={
    "name":"sonu",
    "score":9.6,
    "marks":[1,2,3,4,5],
    "sub":{
        "chem":10,
        "phy":20,
        "math":30 
        }
}
print(dict)
print(dict["sub"])
print(dict["sub"]["chem"])

#4 Dictionary Methods
print(dict.keys())
print(dict.values())
print(dict.items())
pairs=(list(dict.items()))
print(pairs[1])
print(pairs[2])
print(dict.get("name"))
print(dict.get("marks"))
dict1={"age":20}
print(dict.update(dict1))
  
#5 Sets In Python
set1={1,2,2,3,4,'hello','sonu'}
print(set1)
# print(type(set1))
# print(len(set1))
# Null_set=set()
# print(Null_set)
# set1.add(5)
set1.add(5)
print(set1)
set1.remove(2)
print(set1)  
print(set1.pop())
print(set1.pop())
set1.clear()
print(set1)'''
set1={1,2,3,4}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))














































