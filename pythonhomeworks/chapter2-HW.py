number = int(input("Please enter a number between 0 and 20: "))
if 0 <= number <= 20:
    #number = goodnumber
    if number % 2 > 0:
    #if goodnumber % 2 > 0:
        print("%s is not an even number. Please try again.\n " % number)
    else:
        print("%s is indeed an even number. Nice work, chump!" % number)

else:
    print("I said between 0 and 20, clown! Pay attention!")