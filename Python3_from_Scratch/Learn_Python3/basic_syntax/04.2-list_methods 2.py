cars = ["bmw", "audi", "honda"]

print("*" * 22 + "length " + "*"*22 )
#length calculates the length of the list which is basically how many items in said list

length=len(cars)
print(length)
#This should return 3 because there are 3 cars in the list
print("*" * 22 + " .append " + "*"*22 )


#.append method appends an item to to the END of the list
cars.append("Benz")
print(cars)
#Should return the same list with "Benz" added to the end
print("*" * 22 + " .insert " + "*"*22 )

#.insert method inserts the given item at the provided location (index) moving every other item after it back
cars.insert(1, "Jeep")
print(cars)
#Should return the car list with jeep added at index 1
print("*" * 22 + " .index " + "*"*22 )

#.index method allows us to check the index of the specified item
myindex = cars.index("honda")
print(myindex)
#Should return the index of "honda" in cars list at that time
#Note: Is there are 2 instances of the specified item it will give the index of the first instane
print("*" * 22 + " .pop " + "*"*22 )

#.pop method by default, allows the removal of the last item in the list
removeone = cars.pop()
print(removeone)
print(cars)
#First print should return the last item in the list
#Should return the cars list minus the last item in it
print("*" * 22 + " .remove " + "*"*22 )

#.remove method allows the removal of specified item from the list
cars.remove("Jeep")
print(cars)
#Should return the list minus "list"
print("*" * 22 + " Slicing " + "*"*22 )

#Slice methos allows the slicing of a list starting at a given point
slicing = cars[0:2]
print(slicing)
#This will return the item at index 0 and 1 as 0 is inclusive and 2 is exclusive. If we want item at index 2 we'd write [0:3]
print("*" * 22 + " .sort " + "*"*22 )

#.sort will sort the items in a  list
print(cars)
cars.sort()
print(cars)
print("*" * 44)
