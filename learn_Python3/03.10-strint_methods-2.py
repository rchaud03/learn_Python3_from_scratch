#Replacing characters in a string

stringa="1abc2abc3abc4abc"
#This will orint the string "1abc2abc3abc4abc"
print(stringa)

#This will replace all the abc's with xyz when printing and output "1xyx2xyz3xyz4xyz"
print(stringa.replace("abc", "xyz"))

#Notice it replaced all of them.

#But what if we only wanna replace the first abc thus printing 1xyz2abc3abc4abc
print(stringa.replace("abc", "xyz",1))

#We can assign a variable to a substring
#This  variable assigns the characters at index 1-5 to the variable substringa. The 6th will not be included.
substringa=stringa[1:6]

print(substringa)

#The following will do the same but by intervals of 2. So since the substring we are using is "abc2a" it uses the first character, skips the next 2
stepstringa=stringa[1:6:3]

print(stepstringa)