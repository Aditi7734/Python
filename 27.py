# a=[1,2,3,4,5]
# b=[6,7,8,9]
# print(a[1:4])
# print(a[1:3])
# print(a+b)
# print(a[1:2:3])
# print(a[3])
# a[-1:-1]=[8,9,1]
# print(a)
# print(a*2)
# print(a==b)
# print(4 in a)#aliasing
# a=[1,2,3,4,5,6]
# b=a
# print(a)
# print(b)
# b is a
# a is b
# a[0]=100
# print(a)
# print(b)
# #cloning
# b=a[:]
# print(b)
# [1,2,3,4,5]
# print(a is b)
# b=list(a)
# print(b)
# print(a is b)
a=[1,2,3,4,5]
b=a.copy()
print(a is b)
print(b)
dlist=['red','orange','blue','green','yellow']
print(dlist)
del dlist[3]
print(dlist)
dlist.remove('orange')
print(dlist)
elem=dlist.pop(-1)
print(elem)