# #recursion:calling a function itself or again and again
# def factorial(x):
#     """This is recursive function to find the factorial"""
#     if (x==1 or x==0):
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=3
# print("the factorial of",num,"is",factorial(num))
# #print the fibnocci series using recursion#python do not support function overloading
# x=input("x")
# def add(x,y)

#     print(x+y)
# add(x,y)
def add(datatype,*args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ''
    for x in args:
        answer = answer + x
        print(answer)
        add('int',5,6)
        add('str',a,b)
class Animal:
    name = ""
    def eat(self):
        print("I can eat")
    class Dog(Animal):
        def display(self):
            print("my name is",self.name)
        
labrador = dog()
labrador.name