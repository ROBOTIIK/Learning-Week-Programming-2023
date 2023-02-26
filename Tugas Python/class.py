class University:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Student(University):
    def __init__(self, name, id_number, courses):
        self.courses = courses
        University.__init__(self, name, id_number)

class Professor(University):
    def __init__(self, name, id_number, courses_taught):
        self.courses_taught = courses_taught
        University.__init__(self, name, id_number)

s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)