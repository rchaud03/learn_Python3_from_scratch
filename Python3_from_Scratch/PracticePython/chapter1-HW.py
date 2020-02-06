import datetime

now = datetime.datetime.now()
name = input("Please enter you name: ")
print("Thank you %s!" %name)
age = int(input("Now please tell us your age: "))
print("So as of %s, %s is %s years old" %(now.year, name, age))

to100 = 100 - age
turn100 = to100 + now.year
#print("I'm guessing %s will turn 100 years old in the year %s." %(name, turn100))
howmany = int(input("How many times should i print the message about yor age: "))

print(("I'm guessing %s will turn 100 years old in the year %s.\n" %(name, turn100)) * howmany)
