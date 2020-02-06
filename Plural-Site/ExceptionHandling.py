student = {
	"name": "Ronald",
	“student_ID": 321456,
	"Current_Major": None
}

try:
    last_name = student["last_name"]
except KeyError:
	print("Error finding last_name in dictionary")
print("The rest of the code will execute")