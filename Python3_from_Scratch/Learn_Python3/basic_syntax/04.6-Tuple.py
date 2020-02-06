"""
Tuple
Similar to list but cannot be changed
They are expressed using parantheses ()
"""

my_list = [1,2,3]

my_tuple = (1, 2, 3, 2, 2, 3)

#printing list  and tuple
print("Printing list" + "*"*5 + "\n")
print(my_list)
print("Printing tuple" + "*"*5 + "\n")
print(my_tuple)

print("Printing tuple item index 0" + "*"*5 + "\n")
#Printing items at various indexes
print(my_tuple[0])
print("Printing tuple items starting at index 1" + "*"*5 + "\n")
print(my_tuple[1:])


#Print the index of an item in a tuple
print("Printing the index of an item item in a tuple" + "*"*5 + "\n")
print(my_tuple.index(2))


#Pring how many times an item appears in a tuple
print("Counting how many times an item shows up in a tuple" + "*"*5 + "\n")
print(my_tuple.count(3))