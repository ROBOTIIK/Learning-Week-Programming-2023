class UB_campus:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
class Student:
    def __init__(self, name, id_number, courses):
        UB_campus.__init__(self, name, id_number)
        self.courses = courses
    
class Professor:
    def __init__(self, name, id_number, courses_taught):
        UB_campus.__init__(self, name, id_number)
        self.courses_taught = courses_taught

s = Student("Alfi", 1817, ["Cybersecurtiy", "OSINT Analytics"])
p = Professor("Tafta", 1717, ["Data Science", "Busisness Intelligence"])

print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)
        