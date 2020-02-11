"""""
Object Oriented Programming
****


Class:
A class is a template that defines the object
You can create a class for anything

"""""

"""""
class Car(object):
    def __init__(self, makeArg, modelArg):
        self.make = makeArg            #self is just the first parameter received to create the object
        self.model = modelArg



c1 = Car('bmw',"5501")
print(c1.make)
print(c1.model)

c2 = Car('benz',"E-Class")
print(c2.make)
print(c2.model)
"""""
class full_name:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

        def name_func():
            print("Good morning %s %s! May we call you %s?" % (self.f_name, self.l_name))


person1 = full_name("Ronald", "Chaudry")
person1.full_name()