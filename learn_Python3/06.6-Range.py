#generating a range from 0-9
print(range(0,10))

#However the above code will not be printed. Simply generates and commits to memory

#To actually print it we need to put the range in a list as seen below
print(list(range(0,10)))

my_range = range(0,10)
print(my_range)
print(type(my_range))
print(list(my_range))

#Print in steps or intervals of 3
my_range3 = range(0,20,3)
print(my_range3)
print(type(my_range3))
print(list(my_range3))

#using range in loops
#Traditional way
listA = [1,2,3,4,5]

for numA in listA:
    print(numA)

#Can also be rewritten list this

for numB in range(0,6):
    print(numB)
