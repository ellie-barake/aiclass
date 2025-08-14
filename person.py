class Person:
    def __init__(self,name,age):
        self.name=name # self.name store the name
        self.age=age # self.age store the age
    def greet(self):
        print(f"I'm {self.name} and I'm {self.age}")

#creating an object or instance of person
individual1=Person("ellie",19)
individual2=Person("pixie",19)
individual3=Person("gift",19)
individual4=Person("john",17)

 #calling the greet method on the object       
individual1.greet()
individual2.greet()
individual3.greet()
individual4.greet()
