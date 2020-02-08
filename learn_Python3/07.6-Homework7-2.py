def net_income(my_gross, my_state):
    #print("Your gross is %s and you live in %s" %(my_gross, my_state))

    state_tax = {"FL": 0, "GA": .04, "TN": .07, "AL": .04, "LA": .04, "SC": .06}

    net_fed = my_gross - (my_gross * .1)

    if my_state in state_tax:
        net_state = net_fed - (net_fed * state_tax[my_state])
        print(" Your net income after state taxes is %s." % net_state)
        return net_state
    else:
        print("State %s is not in our list of states")
        return None

my_gross = int(input("Please enter your gross annual income: "))
my_state = str(input("Please enter your state of residence: "))
net_income(my_gross, my_state)