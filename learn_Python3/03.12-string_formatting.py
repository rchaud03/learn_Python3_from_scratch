city = "Miami"
event = "Concert"

print("Welcome to " + city + " and enjoy the " + event)
#This same pring statement can be rewritten as seen below

print("Welcome to %s and enjoy the %s" %(city, event))

#We can use the same approach when it's just one variable involved
print("Welcome to %s" % city)