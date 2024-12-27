"""
question no 1
str1=str(input("enter a string: "))
str2=str(input("enter a string: "))
a=len(str1);
b=len(str2);
if(a>b):
    print(str2+str1+str2)
elif(b>a):
    print(str1+str2+str1)
else:
    print(str1+str2+str1)"""
    
""" question 2
str1=str(input("enter a string: "))
if(str1.startswith("Python")):
    print(str1)
else:
    print("Python",str1)"""

#reversing a string
"""a=str(input("enter a string: "))
print("After reversing the string: ",a[::-1])"""
#counting substring inside a string
# we count by using count(substring)
"""str1=str(input("Enter a string: "))
print(str1.count("hello"))"""
#printing every character of string twice Important question
"""a=str(input("enter a string: "))
b=len(a)
for b in a:
    print(a)"""

a=str(input("enter a string"))
b=len(a)
if(a%2==0):
    print(a)
    

