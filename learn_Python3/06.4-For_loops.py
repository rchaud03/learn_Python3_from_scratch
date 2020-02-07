
#Printing letters in strings
my_list = "vertical"

for letter in my_list:
    print(letter)

#Printing letters in string Horizontally
my_2ndlist = "horizontal"

for letters in my_2ndlist:
    print(letters, end=' ')

#Printing lists
my_carslist = ["bmw", "honda", "toyota"]

for car in my_carslist:
    print(car.upper(), end=' ')

#Printing from Dictionaries

dict = {"one": 1, "two": 2, "three": 3}

#Printing keys
for number in dict:
    print(number)

#Printing keys and value
for number in dict:
    print(number + " " + str(dict[number]))

#Printing keys and values 2nd method
for number, digits in dict.items():
    #print(number)
    #print(digits)
    print(str(number) + ":" + str(digits))