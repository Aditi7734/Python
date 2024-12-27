# class Student:
#     pass
# Stud_1 = Student()
# Stud_1.name=input("Enter name:")
# Stud_1.branch=input("Enter branch")
# Stud_1.rank=input("Enter rank")
# print("Stud_1.name",Stud_1.name)
# print("Stud_1.branch",Stud_1.branch)
# print("Stud_1.rank",Stud_1.rank)
# class Car:
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         Honda = Car()
# Honda = Car()
# carname = input("car name:")
# Honda.setName(carname)
# print("Honda car name:",Honda.getName())
#unit 5 lesson 3 ques no 1
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# name = input("s1 name")
# age = input("s1 age")
# s1_name = name
# s1_age = age
# Stud_1 = Student(name,age)
# name = input("s2 name")
# age = input("s2 age")
# s2_name = name
# s2_age = age
# Stud_2 = Student(name,age)
# print('stud_1.name',Stud_1.name)
# print("stud_2",Stud_2.name)
#unit 5 lesson 3 question 5
# class Empolyee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def displayEmpolyee(self,name,salary):
#         self.name = name
#         self.salary = salary
# name = input("name: ")
# salary = int(input("salary: "))
# emp = Empolyee(name, salary)
# print(name,salary)
#lesson 4
# class Person:
#     def setname(self,name1):
#         self.name = name1
#     def getname(self):
#          return self.name
# p1 = Person()
# p2 = Person()
# name1 = input("p1 name: ")
# name2 = input("p2 name: ")
# p1.setname (name1)
# p2.getname (name2)    
# print("p1 name:",p1.setname(name))
# print("p2 name: ",p2.getname(name))    
#  class Person:
#      def setname(self, name1):
#          self.name = name1

#      def getname(self):
#          return self.name

# p1 = Person()
# p2 = Person()

# name1 = input("p1 name: ")
# name2 = input("p2 name: ")

# p1.setname(name1)
# p2.setname(name2)

# print("p1 name:", p1.getname())
# print("p2 name:", p2.getname())
# class Person:
#     def setname(self,name):
#         self.name = name
#     def getname(self):
#         print(self.name)
# class Student(Person):
#     def setage(self,age):
#         self.age = age
#     def getage(self,age):
#         print(self.age)
# name = input("please enter a name:")
# age = int((input("please enter age: ")))
# s1 = Student()
# s1.setname(name)
# s1.setage(age)
# s1.getname()
# s1.getage()
# unit 5 lesson 5
# class Person:
#     def setname(self, name):
#         self.name = name

#     def getname(self):
#         print(self.name)


# class Student(Person):
#     def setage(self, age):
#         self.age = age

#     def getage(self):
#         print(self.age)

# # Input from the user
# name = input("Please enter a name: ")
# age = int(input("Please enter age: "))

# # Create an instance of the Student class
# s1 = Student()

# # Set the name and age using the set methods
# s1.setname(name)
# s1.setage(age)

# # Get and print the name and age
# s1.getname()
# s1.getage()
# class Car:
#     def setbrandname(self, brandname):
#         self.brandname = brandname
#     def setmodel(self,model):
#         self.model = model
#     def getmodel(self):
#         print(self.model)
# class Accord(Car):
#     def setbrandname(self, brandname):
#         self.brandname = brandname
#     def getbrandname(self):
#         print(self.brandname)
# blueaccord = Accord()
# brand = input("brand:")
# model = input("model:")
# blueaccord.setbrandname(brand)
# blueaccord.setmodel(model)
# blueaccord.getbrandname()
# blueaccord.getmodel()
# 
import re
txt="the rain in spain"
x=re.findall("[a-m]",txt)
print(x)

txt="hello planet"
x=re.findall("^hello",txt)
if x:
    print("yes, the string start with 'hello'")
else:
    print("No match")
txt="planet hero"
x=re.findall("he.*o",txt)
s='Readablity counts.'
pattern = r'[aeiou]'
matches = re.finditer(pattern,s)
for match in matches:
    print(match)
txt="2020 - 2025 - 2050 # this is a phone number"
x=re.findall("#.*$",txt)
print(x)
txt="2020-2025-2050"
x=re.findall("\D",txt)
print(x)
x=re.findall("\D")
txt="simple is better than complex and complex is better than complicated"
pattern = r'[is]'
x=re.findall("was",txt)
# print(x)
# txt="w3school.com"