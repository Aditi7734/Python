# program to finding wether the given year is leap year or not
#year = int(input("Year: "))


    
'''if Year%100 and Year%400!=0 :
    print("NO Leap")
elif Year%4==0 :
    print("leap Year")
    
else:
    print("Leap Year")'''
    
    
'''if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''
    
    
''' couning wether a number inside list is positive or not
num=[1,4,-9,8,-4,-8,0,8,4]
count=0
for a in num:
    if a > 0:
        count+=1
print("Final count of ",count)'''

'''a=int(input("enter a even number: "))
sum = 0
for i in range(1, a+1):
    
    if i%2==0:
        sum+=i
print("sum",sum)'''

'''a= int(input("Enter an even number: "))

sum=0
count = 1

while count <=a :
    if count % 2 == 0:
        sum += count
        count += 1
        
print ("sum: ",sum)'''
'''a=int(input("a: "))
b=int(input("b: "))
while(b>0):
    r=a%b
    a=b
    b=r
GCD=a
print("GCD: ",GCD)'''

'''#fibnocci series

n=0
n1=1
i=1
num=int(input("num: "))
while(i<=num):
    sum=n+n1
    print(sum)
    n=n1
    n1=sum
    i=i+1'''
    

'''a=int(input("a: "))
for i in  range(1,11):
    result=a*i
    print(f"{a}*{i}=",result)
    ()'''
    
'''#find prime number between x and y
a=int(input("a: "))
b=int(input("b: "))
count=1
for i in range(a, b):
    if i==2 :
        count=count+1
    elif i>2 and i%2 !=0:
        prime = True
        
        for j in range(3, int(i**0.5)+1, 2):
            if i%j == 0:
                prime = False
                break
        if prime :
            count = count+1

print(count)    '''

'''#Armstrong number sum of power of no of digit 
a=int(input("enter the digit to check armstrong number: "))
#count how many digit is present in number
count = 0
sum=0
if(a==0):
    print("1")

while(a>0):
    x=a%10
    sum=sum+x
    a=a//10
    
   

print("sum of digit is: ",sum)'''
'''#largest of three number
a=int(input("num1: "))
b=int(input("num2: "))
c=int(input("num3: "))
if a>b and a>c:
    print("num1 is greatest of all")
elif b>a and b>c:
    print("num2 is greatest of all")
else:
    print("num3 is greatest of all")'''
    
'''#check wether it is armstrong number or not
a=int(input("number to check: "))
original=a
temp=a
count=0
while(temp>0): 
    temp=temp//10
    count+=1
    
sum=0
temp=a
while(temp>0):
   x= temp%10
   sum+=x**count
   temp=temp//10

if(sum==original):
    print("congrats its armstrong number!")
    print("here is the sum: ",sum)
else:
    print("oops try next time!")    '''
    
    
'''def floyds_triangle_pattern():
    word = "PYTHON"  # The word to print
    length = len(word)  # Get the length of the word

    for i in range(length, 0, -1):  # Loop from length to 1 (decreasing)
        for j in range(i):  # Loop to print characters
            print(word[j], end=' ')  # Print the character followed by a space
        print()  # Move to the next line

# Call the function to print the pattern
floyds_triangle_pattern()
'''
'''num=1
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print(num,end=' ')
            num=num+1
        else:
            print(" ",end='')
    print()'''
    
'''n=5
for i in range(n):
    print(' '*(n-i),end='')
    
    value = 1
    for j in range(i+1):
        print(value, end=' ')
        value=value*(i-j)//(j+1) #binomial coefficent formulae
    print()
    '''

#practice 
#question 1 leap year problem
'''
year=int(input("year: "))
if(year%4==0 and (year%100!=0 or year % 400 == 0)): #main logic for leap year
    print("you entered leap year.")
else:
    print("not leap year")
''' 
#question 2 sum of even number

'''n=int(input("enter a number: "))
sum=0
i=2
while(i <=n):
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)    
'''
#question 3
'''a=int(input("num: "))
original=a
count=0
while(a>0):
    a=a//10
    count+=1

a=original
sum=0
while(a>0):
    digit=a%10
    sum=sum+digit**count
    a=a//10
    

    
if(sum==original):
    print("armstrong number")
else:
    print("not armstrong number")'''
        

'''#fibnocci series
num=int(input("num: "))
a=0
b=1
i=0
while(i<=num):
    sum=a+b
    print(sum)
    a=b
    b=sum
    i=i+1'''
    
'''a=input("ch: ")
b="aeiouAEIOU"
c=list(b)
if a in c:
    print("vowel")
elif a.isalpha():
    print("consonant")
else:
    print("not an alphabet")'''
    
#pattern
'''num=1
for i in range(1,6):
    for j in range(1,6):
        if(j>=i):
             
            print(num,end=" ")
            num=num+1
        else:
            print(" ",end=' ')
    print()'''
    
'''n=6
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

'''import math
n=int(input("rows: "))
for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for k in range(i+1):
print(factorial(i)//(factorial(k)*))'''

#floyds triangle
'''n=int(input("enter n: "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=' ')
        num+=1
    print()'''

#reverse
'''n=5
for i in range(n,0,-1):
    for j in range (i, 0, -1):
        print(j, end = " ")
    print()'''

'''n=5
for i in range (n):
    print(" "*(n-i), end=" ")
    
    num=1
    for j in range(i+1):
        print(num,end=" ")
        
        num = num*(i-j)//(j+1 )
    print()        '''
print("hello")