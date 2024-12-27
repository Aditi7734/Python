x=input("x")
print(x[0:2:]+x[-2:])
if len(x)<=3:
    print(x)
#repetition
a=input("str:")
b=int (input("n:"))
print(a*b)
#immutable
str="hello world"
newstr="j"+str[5:]
print(str[:4]+"w"+str[5:])
#captalize method,upper(),swapcase(),split(),center(width,"fillchar"),count()
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.title())
print(str.swapcase())
print(str.split())
print(str.center(30,"*"))
#s="happy married life"
#print(s.count('happy'))
#print(str.replace('world','engineers'))
#b=''
#list1=["hi", 'hello','bye']
#print(b.join[list1])
print(str.isupper())
print(str.islower())
print(str.isalpha())
print(str.isalnum())
print(str.isdigit())
print(str.isspace())
#j=input("str1;")
#h=input("str2:")
#print(j*(h(*3)))
print("it\'s very powerful")
print("we can represent string using \"")
print("hello\tpython")
print(repr(str))
print(min(a))
print(max(a))
 