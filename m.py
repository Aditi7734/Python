#str:input("str")
#if (str.startswith("python")and str.endswith("programming")):
   # print("valid")
#else:
 #   print("invalid")
import string
print(string.punctuation)
print(string.digits)
print(string.printable)
print(string.capwords('hello python'))
print(string.hexdigits)
print(string.octdigits)
str=input("input:")
nstr=""
for i in str:
    j=i*2
    nstr+=j
    print(nstr)
print(str.isprintable())
    
data=input("data")
print(data.split())
print(type(data))