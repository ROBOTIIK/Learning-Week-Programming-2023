class Student:
    def __init__(self, nama, id_number, course):
        self.nama = nama
        self.id_number = id_number
        self.course = course
Student = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
class Professor:
    def __init__(self, nama, id_number, course_taught):
        self.nama = nama
        self.id_number = id_number
        self.course_taught = course_taught
Professor = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(Student.nama, Student.id_number, Student.course)
print(Professor.nama, Professor.id_number, Professor.course_taught)