# class Phone:
#     def make_call(self):
#         print("making phone call")
#     def play_game(self):
#         print("playing game")
# p1=phone()
# p1.make_call()
# class Phone:
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost
#     def make_call(self):
#         print("play a game")
#  p2 = Phone()
#  p2.set_color("blue")   
#  p2.set_cost(5000)
#  p2.show_color()
#  p2.show_cost()
#  p2.play_game()
class Employee:
     def __init__(self,name,age,gender,salary): 
         self.name=name
         self.age=age
         self.gender=gender
         self.salary=salary
     def show_empolyee_details(self):
            print("name of empolyee",self.name)
            print("age of empolyee",self.age)
            print("gender of empolyee",self.gender)
            print("salary of empolyee",self.salary)
e1 = Employee("Suresh",27,'male','400000')
e1.show_empolyee_details()