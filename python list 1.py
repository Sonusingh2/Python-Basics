1 LIST OPERATION
marks=[94.5,86,87,88]
print(marks)
print(marks[0])
print(marks[1])
print(type(marks))
print(len(marks))
marks[0]=95
print(marks)
2 LIST SLICING
marks =[85,86,87,88,89]
print(marks[1:4])
print(marks[ :4])
print(marks[1: ])
print(marks[-3: ])
3 LIST METHOD
a=[1,2,3]
b=[1,2,3]
c=[1,2,3]
d=[1,2,3]
e=[1,2,3]
f=[1,2,3]
a.append(4)
b.sort()
c.sort(reverse=True)
d.insert(1,5)
e.remove(2)
f.pop(1)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)                                             
#4 TUPLES IN PYTHON
tup=(1,2,3,4,5)
print(type(tup))
print(tup[1])
tup[1]=5 #in tup we can not modify the values
#5 TUPLE METHODS
tup=(1,2,3,4,1,2)
a=tup.index(3)
b=tup.count(1)
print(a)
print(b)






