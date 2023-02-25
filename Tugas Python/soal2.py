 #soal 2
 
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Student(Person):
    def __init__(self, name, id_number, courses):
        super().__init__(name, id_number)
        self.courses = courses
        
class Professor(Person):
    def __init__(self, name, id_number, courses_taught):
        super().__init__(name, id_number)
        self.courses_taught = courses_taught
        
s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])

print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)

 