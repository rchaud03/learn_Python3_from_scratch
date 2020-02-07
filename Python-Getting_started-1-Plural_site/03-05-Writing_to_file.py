students = []

#function1
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        #students_titlecase = student["name"].title()

        #We removed the above because as we read the file when it has more than one name it only prints one
        #The reason for that is the above code just takes the name inserted thus overwriting the value. So we want to append it instead.
        students_titlecase.append(student["name"].title())
    return students_titlecase


#function2 We’ll get this function to call for the returned value from function#1
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


#function3 is passed an argument
def add_student(name,  student_id=332):
    student = {"name": name, "student_id": student_id }
    students.append(student)

#We comment this out once the read/write fucntions were added
#student_list = get_students_titlecase()


#write/append to the students.txt file
def save_file(student):
    try:
            f = open("students.txt", "a")
            f.write(student + "\n" )
            f.close()
    except Exception:
        print("Coukd not SAVE file!")


#read the students.txt file
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
            #students.append(student)
        f.close()
    except Exception:
        print("Could not READ file!")


#code starts running here. Notice the order

#First we read the file to see what students are already listed
read_file()
#Second, we call the print fucntion so the students names from the list are printed on the screen
print_students_titlecase()

#Input Function

student_name = input("Enter the student name: ")
student_id = input("Enter the student ID: ")

#We now call the add function to add the name we inputed
add_student(student_name, student_id)

#Then we call the save function
save_file(student_name)