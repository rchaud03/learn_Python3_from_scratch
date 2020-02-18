"""""
Object Oriented Programming


Class:
A class is a template that defines the object
You can create a class for anything

"""""

class Car(object):
    def __init__(self, make, model):
        self.make = make            #self is just the first parameter received to create the object
        self.model = model



c1 = Car('bmw',"5501")
print(c1.make)
print(c1.model)

c2 = Car('benz',"E-Class")
print(c2.make)
print(c2.model)
