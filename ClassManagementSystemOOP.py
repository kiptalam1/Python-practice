class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Average Score: {self.get_average():.2f}"

class ClassRoom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]
        
    def get_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.get_average() for student in self.students)
        return total_average / len(self.students)

    def __str__(self):
        student_list = "\n".join(str(student) for student in self.students)
        return f"Class: {self.class_name}\nStudents:\n{student_list}\nClass Average: {self.get_class_average():.2f}"

my_class = ClassRoom("Physics 101")

std1 = Student('Adams', '001')
std2 = Student('Anonymous', '002')
std3 = Student('StoopidBoi', '003')
#print(std.name)
std1.add_grade(75)
std1.add_grade(98)
std2.add_grade(56)
std2.add_grade(34)
std3.add_grade(57)
std3.add_grade(13)

my_class.add_student(std1)
my_class.add_student(std2)
my_class.add_student(std3)
my_class.remove_student('003')

print(my_class)
print()
print(std1)
print(std2)
print(std3)

""" OUTPUT:  
Class: Physics 101
Students:
Student: Adams, ID: 001, Average Score: 86.50
Student: Anonymous, ID: 002, Average Score: 45.00
Class Average: 65.75

Student: Adams, ID: 001, Average Score: 86.50
Student: Anonymous, ID: 002, Average Score: 45.00
Student: StoopidBoi, ID: 003, Average Score: 35.00
"""
