def greet_user(username):
    """Display a simple greeting"""
    print("Hello,"+ username+"!")
    
greet_user('RAM')

def display_message(answer):
    """display what you are learning in this chapter"""
    print("what you are learning\n"+answer+"!")
    
display_message('python function')

def favourite_book(book):
    """display information about favourite book"""
    print("one of my favourite books is"+' ' + book +' '+ "in wonderland")
favourite_book('dar')

def describe_pet(animal_type,pet_name):
    """display information about a pet."""
    print("\nI have a" + animal_type + '.')
    print("My"+animal_type+ "'s name is"+ pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('bullie','oreo')
describe_pet(animal_type='cat',pet_name='katty')

def class_info(name,sec='K23TH'):
    print("My name is "+name+"sec is"+sec)
    
class_info(name='ANUJ')

def describe_city(name,country='INDIA'):
  print("a"+name+"and its "+' '+country)

  
  
describe_city('advik')
describe_city('Supriya')
describe_city('hazel',country='America')

class Dog():
    """a simple attempt to model a dog."""
    def __init__(self, name,age):
        """Initializes name and age attributes."""
        self.name=name
        self.age=age
    def sit(self):
        """simulates a dog sitting in response to a command"""
        print(self.name.title()+ "is now sitting.")
    
    def roll_over(self):
        print(self.name.title()+"rolled over!")
        
        
        
        
"""another question"""

class Restaurant:
  def __init__(self,restaurant_name,cuisine_type):
    self.restaurant_name = input("enter the restaurant name: ")
    self.cuisine_type = input("enter the cuisine type: ")
  
  def describe_restaurant(self,restaurant_name,cuisine_type):
    print(restaurant_name)
    print(cuisine_type)

  def open_restaurant(self):
    print("the restaurant is open")
  
restaurant_name = input("enter the restaurant name: ")#instiating
cuisine_type = input("enter the cuisine type: ")
  

a=Restaurant(restaurant_name,cuisine_type)#making object
a.describe_restaurant(restaurant_name,cuisine_type)#calling function using object keep this in mind
a.open_restaurant()



class User:
  def __init__(self,first_name,last_name,contact_number,address):
    self.first_name=input("please enter your name:")
    self.last_name=input("enter last your name: ")
    self.contact_number=int(input("enter contact number: "))
    self.address=input("enter address")

  def describe_user(self):
    print( self.first_name) 
    print(self.last_name) 
    print(self.contact_number)
    print(self.address)

  def greet_user(self):
    print("hello mr/mrs"+self.first_name+self.last_name) 
    
    
    
    
first_name=input("please enter your name:")
last_name=input("enter last your name: ")
contact_number=int(input("enter contact number: "))
address=input("enter address")

a=a.user(first_name,last_name,contact_number,address)   
a.describe_user()
a.greet_user()
        
    