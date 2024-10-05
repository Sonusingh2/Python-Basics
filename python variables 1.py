#1 print("hello world")
name='sonu'
age=20
price=200
#print(name,age,price)
#print("my name is :",name)
#print("my age is:",age)
#age2=age
#print(age2)

#2 types of variables
#print(type(name))
#print(type(age))
#print(type(price))

#3 different data types
a=12
b=12.33
c='sonu'
d=True
e=None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#4 sum in python
a=4
b=6
sum=a+b
#print(sum)

#4 ARITHMETIC OPERATORS
a=6
b=4
sum=a+b
diff=a-b 
div=a/b
mulp=a*b
modulo=a%b
power=a**b
# print(sum)
# print(diff)
# print(div)
# print(mulp)
# print(modulo)
# print(power)

#5 RELATIONAL OPERATORS
equalto=a==b
notequalto=a!=b
greaterorequalto=a>=b
greaterthan=a>b
lessthanorequalto=a<=b
lessthan=a<b
# print(equalto)
# print(notequalto)
# print(greaterorequalto)
# print(greaterthan)
# print(lessthanorequalto)
# print(lessthan)

 #6 ASSIGMENTS OPERATORS
a=5
a+=5
#print(a)
b=5
b-=5
#print(b)
c=5
c*=5
d=5
d/=5
e=5
e**=5
f=5
f%=5
# print(c)
# print(d)
# print(e)
# print(f)

#7 LOGICAL OPERATORS
#a NOT
a=10
b=20
print(not True)
print(not False)
print(not(a>b))
print(not(a==b))
#b AND
print(True and False)
print(True and True)
print((a>b) and (b>a))
print((a<b)and (b>a))
#c OR
print(True or False)
print(a>b or b<a)

#8 TYPE CONVERSION
a='2'
b=3
a=int(a) #here we converted a from string to integer
print(a+b)
c=5
c=str(c) # here we converted integer to string
print(type(c))

#9 INPUT IN PYTHON
# name=input("enter your name :")
# age=int(input("enter your age:"))
# marks=float(input("enter ypur marks:"))
# print("your name is:",name)
# print("your age is :",age)
# print("your marks is :",marks)
a= input('enter no a:')
b=input('enter no b:')
c=a+b
print(c)