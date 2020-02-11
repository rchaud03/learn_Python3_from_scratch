import os
#import fs

#print all available methods in this module
#print(dir(os))

#print(dir(fs))

#os.system('ls ~/Desktop/')
#os.system('ps -ef | grep -i skype | grep -v grep')

"""""
Create directories
"""""

#create a directory and a subdirectory in one command
#os.makedirs('python_module_dir/sub_dir')

"""""
Remove directories
"""""
#remove a directory. Only 1 dir is removed.
#os.rmdir('python_module_dir/sub_dir')

#remove both directories

#os.removedirs('python_module_dir/sub_dir')

"""""
File management
"""""

#os.rename('old_name','new_name')

#get file info such as size, mtime and ctime, etc. Can be combined with datetime module for time data such as mtime and ctime
#print(os.stat("file_path"))

#same as above but specifying size and mtime .stat alone gives you all info mtime ctime size etc
#print(os.stat("file_path").st_size)
#print(os.stat("file_path").st_mtime)

#combining datetime to get human readable format of modtime
#import datetime
from datetime import datetime

os.system('touch file_name')
os.system('echo "This is a test file" > file_name')
print(os.stat("file_name").st_size)
print(os.stat("file_name").st_mtime)
mod_time = os.stat("file_name").st_mtime

#For human readable time using 'import datetime'
#print(datetime.datetime.fromtimestamp(mod_time))

#The below code would work instead of the one above is we simply 'import datetime' and not 'from datetime import datetime'
print(datetime.fromtimestamp(mod_time))


""""
OS WALK

os.walk traverses the file system and prints out the dis, subdirs and files in said directory structure
it does this in a Tuple of 3 values with the dir path, dir name and file names within that path.

You can then use a for loop to list the directories and files

"""
os.walk('/Users/ronald.chaudry/')
for dirpath, dirnames, filenames in os.walk('/Users/ronald.chaudry/Downloads/learnPython3-Bundle/myTestDir/'):
    print("Current path: %s" % dirpath)
    print("Directories: %s" % dirnames)
    print("Files: %s" % filenames)

""""
OS Environment

"""

#Changing directories
os.chdir('/Users/ronald.chaudry/Downloads/learnPython3-Bundle/myTestDir/')

#Printing the home directory
print(os.environ.get('HOME'))

#Combning 2 paths together
file_path2 = os.environ.get('HOME') + 'random_file.txt'
print(file_path2)

#The above will print but MAY be missing a slash.
#It is safe to use the pat.join method to take out the guess work
file_path3 = os.path.join(os.environ.get('HOME'), 'random_file.txt')
print(file_path3)

#.basename gives you just the name of the file
print(os.path.basename('/tmp/test.txt'))

#.dirname gives you the dir name from the file path
print(os.path.dirname('/tmp/test.txt'))

#We can use split the two
print(os.path.split('/tmp/test.txt'))

#Does it exist? Returns true or false
print(os.path.exists('/tmp/test.txt'))

print(dir(os.path))

