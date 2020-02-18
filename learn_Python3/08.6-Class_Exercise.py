"""""
Assignment 8.6: Classes and objects

"""""




class fruit(object):
    def __init__(self):
        print("We're creating a new fruit instance.")


    def nutrition(self):
            print("This fruit is very nutritious!")


    def fruit_shape(self):
        print("The shape of this fruit makes it very easy to hold and conceal.")


class zabriko(fruit):
    def __init__(self):
        print("We just created a zabriko instance")

    def nutrition(self):
        print("Despite what you may think, this fruit is low in sugar content")

    def fruit_shape_color(self):
        print("It's true. This fruit often gets mistaken for a cantaloupe because of its color and shape.")


p = fruit()
p.nutrition()
p.fruit_shape()

z = zabriko()
z.nutrition()
z.fruit_shape_color()

