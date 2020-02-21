#Collect the user's input word
urword = input("Please enter a word that is a palindrome:")

#Spell the collected word backwards
bckword = urword[::-1]

#Check if the user's word and the same word spelled backwards are the same
if urword == bckword:
    print("%s spelled backwords also spells %s" %(urword, bckword))
else:
    print("Sorry %s spelled backwords is not the same as %s and therefore not a palindrome" % (urword, bckword))
#print(bckword)