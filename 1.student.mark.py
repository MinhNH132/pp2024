numberOfStudent = 0
numberOfCourse = 0
students, nameCourses, idCourses, mark = [], [], [], []
marks = {}

#number of student/course
def numberOfStudents():
    global numberOfStudent
    numberOfStudent = input("Enter the number of students: ")
    if (numberOfStudent.isdigit()):
        return numberOfStudent
    else:
        option(10)
        option(1)
def numberOfCourses():
    global numberOfCourse
    numberOfCourse = input("Enter the number of courses: ")
    if (numberOfCourse.isdigit()):
        return numberOfCourse
    else:
        option(10)
        option(2)

#add dict of each student into a list
def infoStudents(students, i):
    for x in range(int(i)):
        student = {"ID": input(f"ID of student number {x+1}: ") ,"name": input(f"Name of student number {x+1}: ") , "DoB": input(f"DoB of student number {x+1}: ")}
        students.append(student)
    
#add courses' name and id into list
def nameOfCourse(nameCourses, idCourses, i):
    for x in range(int(i)):
        nameCourse = input("Enter the name of the course: ")
        nameCourses.append(nameCourse)
        idCourse = input("Enter the id of the course: ")
        idCourses.append(idCourse)
        
#add mark into a list
def enterMark(mark, i):
    for x in range(int(i)):
        mark.append(input(f"Enter the mark of the {x+1} student: "))

#check to see if the course name exist or not
def checkName(courseNames, courseName):
    if courseName in courseNames:
        return True
    else: 
        print(f"{courseName} doesn't exist in the course list!")
        return False
#add list of mark into a whole dict with course name
def enterMarks(courseName, marks, mark):
    marks[courseName] = [mark]

#print students and courses info
def listStudent(i, students):
    for x in range(int(i)):
        print(f"{x+1}. ID: ",students[x]["ID"]," Name: ",students[x]["name"]," DoB: ",students[x]["DoB"])
def listCourse(i, nameCourses, idCourses):
    for x in range(int(i)):
        print(f"{x+1}. Name: ",nameCourses[x]," ID: ",idCourses[x])
        
#get index in dict "marks" 
def getIndex(courseName, marks):
    index = list(marks.keys()).index(courseName)
    return index
#print mark
def printMark(courseName, marks):
    print(f"Mark of students in the course {courseName}")
    print(marks[courseName])
            

        
def option(number):
    global numberOfCourse
    global numberOfStudent
    match number:
        case "1": #enter number of students
            numberOfStudent = numberOfStudents()
            option(input("\nPlease enter the number: "))
        case "2": #enter number of courses
            numberOfCourse = numberOfCourses()
            option(input("\nPlease enter the number: "))
        case "3": #enter info of each students
            if (numberOfStudent != 0):
                infoStudents(students, numberOfStudent)
                option(input("\nPlease enter the number: "))
            else:
                print("Please enter the number of students first!")
                option(1)
        case "4": #enter info of each course
            if (numberOfCourse != 0):
                nameOfCourse(nameCourses, idCourses, numberOfCourse)
                option(input("\nPlease enter the number: "))
            else:
                print("Please enter the number of courses first!")
                option(2)
        case "5": #enter specific course to input mark
            mark = []
            nameCourse = input("Enter the name of course that you want to input mark in: ")
            if (checkName(nameCourses, nameCourse)):           
                enterMark(mark, numberOfStudent)
                enterMarks(nameCourse, marks, mark)
                option(input("\nPlease enter the number: "))
            else: option(input("\nPlease enter the number: "))
        case "6": #list students
            if (numberOfStudent != 0):
                listStudent(numberOfStudent, students)
                option(input("\nPlease enter the number: "))
            else:
                print("There are no student to show!")
                option(input("\nPlease enter the number: "))
        case "7": #list courses
            if (numberOfStudent != 0):
                listCourse(numberOfCourse, nameCourses, idCourses)
                option(input("\nPlease enter the number: "))
            else:
                print("There are no courses to show!")
                option(input("\nPlease enter the number: "))
        case "8": #list marks on specific courses
            nameCourse = input("Enter the name of the course that you want to print out: ")
            if (checkName(nameCourses, nameCourse)):
                printMark(nameCourse, marks)
                option(input("\nPlease enter the number: "))
            else: option(input("\nPlease enter the number: "))
        case "9": #Exist the program
            print("Done!!!")
        case "10": #Error in input data
            print("Invalidate input")
        case default:
            option(input("\nPlease enter the number again: "))
            return "Wrong input"

def main():
    option(input("Enter the number: "))
    
main()