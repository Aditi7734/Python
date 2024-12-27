
# def my_function():
#     print("Hello from a function")
# my_function()
# def add(x,y):
#     s=x+y
#     print(s)
# def sub(x,y):
#     d=x-y
#     print(d)
# def mul(x,y):
#     f=x*y
#     print(f)
# x=int(input("a:"))
# y=int(input("b:"))
# add(x,y)
# sub(x,y)
# mul(x,y)
# def add(a, b):
#     return a+b
# a=int(input("a:"))
# b=int(input("b:"))
# def add(a,b):
#     return a+b
# add(a,b)
# def sub(a,b):
#     return a-b
# sub(a,b)
# print("adddition:",add(a,b))
# print("substraction:",sub(a,b))
# def greet(name):
#     print("hey there")
#     print("welcome",name)
# greet("caleb")
# greet("Aditi")
# greet("Vipul")
# greet("Mohit")
# def sayhello(username):
#     greet="hello"
#     print(greet+""+username)
# users = ['Ram','Mahesh','Vashudha','uma']
# for name in users:
#     sayhello(name)
# def greet(name,age):
#     print(f"my name is {name} and my age is {age}")
# greet(name="ashish",age=23)
    
# def greet(name,dep):
#     print(f"hi {name}")
#     print(f"are you from {dep} department?")
# greet("Aashima","CS")
# def info(name,age):
#     print(f"name is {name} and age is {age}")
    
 
# info("jay",age=34)
# info(name="jay",age=35)
# def fun1(name="padma",age=12):
#     print(name,"is",age,"years old")
# fun1("aruna",16)
# fun1(age=16,name="karuna")
# fun1("padma",16)
# fun1("karuna")
# fun1()
# def mysum(*args):
#     return sum(args)
# print(mysum(2,9,8,5))
# print(mysum(299,900,890))
# def largestnumber(*number):
#     print("largest",max(number))
# largestnumber(3,6,32,56)
# largestnumber(10000,9000)
# #lambda function
# add=lambda a:a+10
# print(add)
# print(add(10))
# greet=lambda:print('hello world')
# greet()
# greet_user=lambda name:print('hey there,',name)
# greet_user('Deliah')
# function1=lambda x,y:x+y
# a=int(input(""))
# b=int(input(""))
# print(function1(a,b))
# nums=[3,4,6,2]
# def square(a):
#     return a*a
    
# mapped=list(map(square,nums ))
# print(mapped)
# for ele in mapped:
#     print(ele)
# list1=[1,2,3,4,5]
# def squares(x):
#     return x**2
# y=print(list(map(squares,list1)))
# print(list(map(lambda x:x**2,list1)))
# print([x**2 for x in list1])
# a=int(input( "a="))
# b=int(input("b="))
# c=int(input("c="))
# def largest(a,b,c):
#     if a>b>c:
#         print("a is largest")
#     elif b>c>a:
#         print("b is largest")
#     else:
#         print("c is largest")
# largest(a,b,c)
# def greet():
#     message='Hello'
#     print("local",message)
# greet()
# message="hello"
# print(message)
# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# n=int(input("enter the value of n"))
# result=square(cube(n))
# print(result)
# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# def find_sum(n):
#     if n==1:
#         return 1
#     return n + find_sum(n-1) #main condition
# #finocci series 0,1,1,2,3,5,8,13
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
a = " hello Python hello"
b="supriya"
print(a[4:1:-1])
print(a[2:5:-1])
print(a[-1::-3])
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.split())
print(a.center(20,"u"))
print(a.count('hello'))
print(a.replace('hello','hi'))
print(a.join(b))
b='.'
l1=["www","codetantra","com"]
print(b.join(l1))
str=input("str: ")
result=""
for i in str:
    result=result+2*i
print("result:",result)

    