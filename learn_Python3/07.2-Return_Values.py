#A return simply returns a value after processing and holds it for further processing wether it's to print or process it otherwise

def num_method(arg1, arg2):
    """""
    Use this space to explain what your code or function does 
    This is not required but just good practice
    """""

    return arg1 + arg2

sum1 = num_method(33,55)
sum2 = num_method(44,87)

print(sum1)
print(sum2)

def ismetro(city):
    citylist = ["nyc", "miami", "lax", "atlanta"]
    if city in citylist:
        #return True
        print("Yes, %s is in the metro city list" % city)
        return True
    else:
        #return False
        print("Sorry, %s is not on our metro city list" % city)
        return False

mycity = ismetro("mia")
print(mycity)

mycity2 = ismetro("boston")
print(mycity2)



