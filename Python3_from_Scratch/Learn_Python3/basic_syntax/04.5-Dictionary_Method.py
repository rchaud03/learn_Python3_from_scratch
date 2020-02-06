car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

#printing the Keys from the dictionaries
print(car.keys())
print(cars.keys())

print(car.values())
print(cars.values())

#printing entire keyvalue pairs (items)
print(car.items())
print(cars.items())

#Copying a dictionary
car_copy = car.copy()
print(car_copy)

#Emptying a dictionary
#car_empty = car.clear()
#print(car_empty)

#Pop
print(car.pop("model"))
print(car)
