#--------Class person--------------------------
class person():
    def __init__(self, name):
        self.name = name
        
#-------Class student dengan tambahan id_number dan courses----------
class student(person):
    def __init__(self, name, id_number, courses):
        super().__init__(name)
        self.id_number = id_number
        self.courses = courses

#-------Class professor dengan tambahan id_number professor dan courses_taught---------
class professor(person):
    def __init__(self, name, id_number, courses_taught):
        super().__init__(name)
        self.id_number = id_number
        self.courses_taught = courses_taught

#--------Test Cases-----------------------------------------------------------------------
s = student("Alice", 1234, ["Introduction to Computer science", "Data Structure"])
p = professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)