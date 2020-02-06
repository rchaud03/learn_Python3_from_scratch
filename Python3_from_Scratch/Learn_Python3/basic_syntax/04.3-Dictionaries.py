cars = {"make": "bmw", "model": "350i", "year": 2016}
print("*" * 22 + " Printing car dictionary " + "*"*22 )
print(cars)

print("*" * 12 + " Printing specific value from car dictionary  " + "*"*12 )
#We can print specifc values from the dictionary keypairs by using the key
model = cars["model"]
print(cars["year"])
print(model)

print("*" * 12 + " Printing emptyDic  " + "*"*12 )
#We can define an empty dictionary
emptyDic = {}
print(emptyDic)

print("*" * 12 + " Printing emptyDic once keypairs added  " + "*"*12 )
#We can then add key:value pairs using the using the follwong syntax
emptyDic["one"] = 1
emptyDic["two"] = 2

print(emptyDic)

#Here we  sum up an integer with the value in a key
print("*" * 12 + " Performing calculations with values  " + "*"*12 )
sum_1 = emptyDic["two"] + 8
print(emptyDic)

print("*" * 12 + " Replacing the value in emptyDic  " + "*"*12 )
#The two codes below do the same thing
#emptyDic["two"] =sum_1
emptyDic["two"] = emptyDic["two"] + 8

print(sum_1)
print(emptyDic)