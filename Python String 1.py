# 1 Addition of strings
# a="hello"
# b='world'
# print(a+b)
# c=a+" "+b
# print(c)

#2 ADDING NEXT LINE TO SENTENCE
# a="i am boy.My name is sonu"
# a="i am boy.\nMy name is sonu"
# print(a)

#3 ADDING SPACE BETWEN SENTENCE
# a="i am boy.My name is sonu"
# a="i am boy.\tMy name is sonu"
# print(a)

#4 FINDING LENGTH OF STRINGS
# a="iamboy"
# print(len(a))

#5 INDEXING OF STRING
# a="sonusingh"
# #a[1]='k' #we can't modify indexing name
# b=a[0]
# c=a[1]
# #d=a[], # we can't leave box blank
# print(b)
# print(c)

#6 SLICING
# a="sonusingh" #a[star index:ending index]
# b=a[1:4]
# print(b)
# c=a[ :4] #same as a[0:4]
# d=a[1: ] #same as a[1:len(a)]
# print(c)
# print(d)

#7 NEGATIVE SLICING
a="sonusingh"
b=a[-3:-1]
print(b)

#8 STRING FUNCTION
# a="i am sonu singh"
# b=a.endswith("gh")
# c=a.capitalize()
# d=a.replace("sonu","monu")
# e=a.find("am")
# f=a.count("am")
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

#9 CONDITONAL STATEMENTS

#1 Simple one
# age=21
# if(age>=18):
#     print("can vote") # the 4 line gap in starting is called indentation
# else:
#     print("cannot vote")

#2 Students Grades
#9marks=int(input("enter marks:"))
# if(marks>=90):
#     grade="A" 
# if(marks>=80 and marks<90):
#     grade="B"
# if(marks>=70 and marks<80):
#     grade="c"
# else:
#     grade="d" 
# print("students grade is:",grade)

#3 NESTING
# age=int(input("enter your age:"))
# if(age>=18):
#     if(age>=80):
#         print("cannot vote")
#     else:
#         print("can vote")
# else:
#     print("cannot vote")

#4 write a code to find greatest no among 4
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
if(a>=b and a>=b and a>=c and a>=d):
    print("a is greatest no")
elif( b>=c and b>=d):
    print("b is greatest no")
elif(c>d):
    print("c is greatest no")
else:
    print("d is greatest no")
    





























