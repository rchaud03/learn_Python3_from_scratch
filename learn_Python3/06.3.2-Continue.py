"""""
age = 0
while age < 21:
    print("He is only %s" % str(age))
    #print("He is not 21.")
    age = age + 1
    if age == 21:
        break
    #print("Finally he is able to buy beer since he is %s years old" % str(age))
    print("He cannot buy beer until he is not 21.")

else:
    print("Only printing because the age set is greater than 21 which is unlikely")
"""""
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        continue
    print("This example is awesome")
    print("*"*20)
else:
    print("Just broke out of the loop")
    
