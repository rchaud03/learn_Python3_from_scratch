students = []

#function1
def get_students_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase = student["name"].title()
	return students_titlecase

# Note we replaced
#        students_titlecase = student.title()
#   With the following
#        students_titlecase = student[“name”].title()
# This is because student no longer just accepts strings but represents an entire dictionary so we must specify WHAT we want from the dictionary


#function2 We’ll get this function to call for the returned value from function#1
def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


#function3 is passed an argument
def add_student(name,  student_id=332):
    student = {"name": name, "student_id": student_id }
    students.append(student)

student_list = get_students_titlecase()


#Input Function
#We’ll use the input function to add students to the students dictionary that’s defined.

new_student = input("Would you like to add a new student?: ")
if new_student == "yes":
	student_name = input("Enter the student name: ")
	student_id = input("Enter the student ID: ")
elif new_student == "no":
		print("You typed 'no'. Exiting the program.")
		exit()
else:
		print("Please answer by typing 'yes' or 'no' all in lowercase. Exiting...")
		exit()



add_student(student_name, student_id)
print_students_titlecase()

#I added this line to see what the studens dictionary looked like at this point
print(students)
