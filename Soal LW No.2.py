class FilkomUB:
  def __init__(self, name, id_number):
    self.name = name
    self.id_number = id_number

class Student(FilkomUB):
    def __init__(self, name, id_number, course):
      FilkomUB.__init__(self, name, id_number)
      self.course = course
      
class Professor(FilkomUB):
    def __init__(self, name, id_number, course_taught):
      FilkomUB.__init__(self, name, id_number)
      self.course_taught = course_taught

s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])

print(s.name, s.id_number, s.course)
print(p.name, p.id_number, p.course_taught)

