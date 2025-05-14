# CS 301 Assignment Week 2:
# Member 1: Jair Rodriguez
# Member 2: Aaron Chavez
# Member 3: Carina Fierro-Hernandez
# Member 4: Jenna Suits
# Member 5: Javier A. Arroyo-Solis
class User:
    def __init__(self, name, phone_no, user_id, dob):
        self.name = name
        self.phone_no = phone_no
        self.user_id = user_id
        self.dob = dob
    def getInfo(self):
        print("Name: " + self.name)
        print("Phone No: " + self.phone_no)
        print("Email Address: " + self.user_id)
        print("Date of Birth: " + self.dob)
class Course:
    def __init__(self, name, code, dept, completed, instructor, semester,
    enrolled_students):
        self.name = name
        self.code = code
        self.dept = dept
        self.completed = completed
        self.instructor = instructor
        self.semester = semester
        self.enrolled_students = enrolled_students
    def getStudent(self):
        return [student_name.name for student_name in self.enrolled_students]
    def addStudent(self, student):
        counter = len(self.enrolled_students)
        self.enrolled_students.append(student)
        if len(self.enrolled_students) != counter:
            return True
        else:
            return False
    def removeStudent(self, student):
        counter = len(self.enrolled_students)
        self.enrolled_students.remove(student)
        if len(self.enrolled_students) != counter:
            return True
        else:
            return False
    def setInstructor(self, instructor):
        if instructor.dept == self.dept:
            self.instructor = instructor
            instructor.courses_teaching.append(self)
            return True
        else:
            return False
    def getInfo(self):
        print("Course Name: " + self.name)
        print("Course Code: " + self.code)
        if self.instructor is None:
            print("Course Instructor: None")
        else:
            print("Course Instructor: " + self.instructor.name)
            print("Semester Offered: " + self.semester)
        if self.completed:
            print("Course Completed: Yes")
        else:
            print("Course Completed: No")
class Student(User):
    def __init__(self, name, phone_no, user_id, dob, major, dept,
    completed_courses, current_course):
        super().__init__(name, phone_no, user_id, dob)
        self.major = major
        self.dept = dept
        self.completed_courses = completed_courses
        self.current_course = current_course
    def getInfo(self):
        super().getInfo()
        print("Declared Major: " + self.major)
        print("Department: " + self.dept)
    def canEnroll(self, course):
        completed_codes = []
        for c in self.completed_courses: # c stands for course
            completed_codes.append(c.code)
        if course.dept == self.dept and course.code not in completed_codes:
            return True
        else:
            return False
    def getCurrentCourses(self):
        return [course_name.name for course_name in self.current_course]
    def addCourse(self, course):
        if len(self.current_course) < 6:
            counter = len(self.current_course)
            self.current_course.append(course)
            course.enrolled_students.append(self)
        if len(self.current_course) != counter:
            return True
        else:
            return False
    def removeCourse(self, course):
        if len(self.current_course) > 1:
            counter = len(self.current_course)
            self.current_course.remove(course)
        if len(self.current_course) != counter:
            return True
        else:
            return False
class Professor(User):
    def __init__(self, name, phone_no, user_id, dob, dept, designation,
    courses_taught, courses_teaching):
        super().__init__(name, phone_no, user_id, dob)
        self.dept = dept
        self.designation = designation
        self.courses_taught = courses_taught
        self.courses_teaching = courses_teaching
    def getInfo(self):
        super().getInfo()
        print("Designation: " + self.designation + " Professor")
        print("Department: " + self.dept)
    def canTeach(self, course):
        if course.dept == self.dept:
            return True
        else:
            return False
    def getCurrentLoad(self):
        return [course_name.name for course_name in self.courses_teaching]
    def enrollStudent(self, student, course):
        if course not in student.completed_courses:
            s_counter = len(student.current_course)
            c_counter = len(course.enrolled_students)
            student.current_course.append(course)
            course.enrolled_students.append(student)
        if s_counter != len(student.current_course) and c_counter != len(course.enrolled_students):
            return True
        else:
            return False
def passStudent(self, student, course):
    if student in course.enrolled_students:
        completed_counter = len(student.completed_courses)
        current_counter = len(student.current_course)
        student.completed_courses.append(course)
        student.current_course.remove(course)
    if completed_counter != len(student.completed_courses) and current_counter != len(student.current_course):
        return True
    else:
        return False
def failStudent(self, student, course):
    if student in course.enrolled_students:
        current_counter = len(student.current_course)
        student.current_course.remove(course)
    if current_counter != len(student.current_course):
        return True
    else:
        return False
def completeCourse(self, course):
    comp_counter = course.completed
    cour_counter = len(self.courses_taught)
    course.completed = True
    self.courses_taught.append(course)
    if comp_counter != course.completed and cour_counter != len(self.courses_taught):
        return True
    else:
        return False
# Course, Professor, and Student objects I made for testing my code
math = Course("Math", "123", "MATH", False, None, "Spring", [])
english = Course("English", "124", "ENG", False, None, "Spring", [])
science = Course("Science", "125", "SCI", False, None, "Spring", [])
history = Course("History", "126", "HIS", False, None, "Spring", [])
art = Course("Art", "127", "ART", False, None, "Spring", [])
prof_1 = Professor("Mike", "970-123", "Gmail", "1990", "MATH", "Assistant", [], [])
prof_2 = Professor("Kate", "970-234", "Gmail", "1990", "HIS", "Associate", [], [])
prof_3 = Professor("Sam", "970-345", "Gmail", "1990", "ART", "Full", [], [])
student_1 = Student("Rick", "970-456", "Gmail", "2002", "MATH", "MATH", [], [])
student_2 = Student("Petty", "970-567", "Gmail", "2002", "ENG", "ENG", [], [])
student_3 = Student("Wyatt", "970-678", "Gmail", "2002", "HIS", "HIS", [], [])
