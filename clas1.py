class Girls:
    rno=123
    branch="cse" 
    name="abc"
    def read(self):
        rno=345
        print("roll no",rno)
        print("reading")
        print("instance variable",self.rno)
    def write(self):
        print("writing")
    
#creating object to access the data and methods or functions
Riya=Girls()
obj=Girls()
print("rno",Riya.rno)
print("name=",Riya.name)
print("branch=",Riya.branch)
Riya.read()
