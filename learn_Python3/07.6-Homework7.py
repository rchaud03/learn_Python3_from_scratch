

def s_witheld(your_gross,your_state):
    if your_state == "FL":
        statetax = 0
        return your_gross * statetax
    elif your_state == "GA":
        statetac = .06
        return your_gross * statetax
    elif your_state == "TX":
        statetax = 0
        return your_gross * statetax
    else:
        statetax = .17
        return your_gross * statetax

def f_witheld(your_gross):
    f_rate = .1
    return f_rate * your_gross

def your_net(your_gross, after_state, after_fed):
    return your_gross - s_witheld(your_gross, your_state) - f_witheld(your_gross)

your_gross = int(input("Please enter your annual gross income: "))
your_state = str(input("PLease enter the state where you work: "))

#calling the above functions
after_state = s_witheld(your_gross, your_state)
after_fed = f_witheld(your_gross)
take_home = your_net(your_gross, after_state, after_fed)
print("You paid %s in state taxes." % after_state)
print("You paid %s in federal taxes" % after_fed)
print("You took home close to %s." % take_home)

