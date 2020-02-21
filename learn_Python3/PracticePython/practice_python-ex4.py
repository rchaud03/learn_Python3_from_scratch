#Defines range to pick number from
ourrange = range(1,100)


#Prompt user for number between 0 and our range
urnumber = int(input("\nHey!\nWelcome!\nPlease enter a random number between 0 and %s: " % ourrange))

#Empty list where the results will be appended
divisor_list = []

#Check if number falls within range
if urnumber not in ourrange:
    print("We said between 0 and 100.")
else:
    #create new range to divide by
    newrange = range(1,urnumber + 1)
    print("Good Job! \nNow let us process this number using our algorithm. \n")
    for i in newrange:
        divisor = urnumber % i
        if divisor == 0:
            print("%s is a divisor of %s" % (i,urnumber) )
            divisor_list.append(i)
    print(divisor_list)

        #else:
        #    print("Nope")

#print(divisor_list)

