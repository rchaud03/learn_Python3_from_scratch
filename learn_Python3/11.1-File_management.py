"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = [1, 2, 3]

my_file = open("11.1-write_to_file.txt", "w")

for item in my_list:
    my_file.write(str(item))
    #The code below does the same thing but writes each item in a seperate line thanks to the "\n"
    #my_file.write(str(item) + "\n")


my_file.close()