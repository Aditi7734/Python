name = ['Rishika','Bhanu','Ishnoor','Aditya']
print("hello"+' '+ name[0])
print("what's up"+' '+ name[1])
print("hi"+' ' + name[2])
print("hi bro"+' '+ name[3])
#list of favourite mode of transportation
fav_mode = ["gang bicyle","bullet","lamburgini","inova","hero honda","tata","farari","indica","range rover","duke","mahindra thar","mahindra scorpio"]
print("i would like to own a "+' '+ fav_mode[0])
print("i would like to own a "+' '+ fav_mode[1])
print("i would like to own a "+' '+ fav_mode[2])
print("i would like to own a "+' '+ fav_mode[3])
print("i would like to own a "+' '+ fav_mode[4])
print("i would like to own a "+' '+ fav_mode[5])
print("i would like to own a "+' '+ fav_mode[6])
print("i would like to own a "+' '+ fav_mode[7])
print("i would like to own a "+' '+ fav_mode[8])
print("i would like to own a "+' '+ fav_mode[9])
print("i would like to own a "+' '+ fav_mode[10])
guest = ["YATIN","SARJ","PURIT"]
print(guest[0] +' '+"it will be honour to have you in my happiness")

alien_0 ={'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

class Rectangle ():
  def __init__(self,l,b):
    self.length = l
    self.brearh = b

  def perimeter():
    print(2*(self.length+self.breath))

a=Rectangle()
a.perimeter(l,b)


def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
 musician = get_formatted_name('jimi', 'hendrix')
print(musician)
class car():
  """A simple attempt to represent a car."""
  def __init__(self,make,model,year):
    """Return a neatly formatted descriptive name."""
    long_name = str(self.year) + ' '+ self.make + ' '+self.model   
    return long_name.title()
  
my_new_car = car('audi','a4',2016)
print(my_new_car.get_descriptive_name())