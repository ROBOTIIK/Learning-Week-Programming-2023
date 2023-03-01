class akademisi:
    def __init__(self,name, id_number):
        self.__name = name
        self.__id_number = id_number

    @property
    def name(self):
        pass

    @property
    def id_number(self):
        pass

    @name.getter
    def name(self):
        return self.__name
    
    @id_number.getter
    def id_number(self):
        return self.__id_number

class Student(akademisi):
    def __init__(self, name, id_number, course):
        super().__init__(name, id_number)

        self.courses = course


class Professor(akademisi):
    def __init__(self, name, id_number, courses_taught):
        super().__init__(name, id_number)

        self.courses_taught = courses_taught



s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
print(s.name, s.id_number, s.courses)
print(p.name, p.id_number, p.courses_taught)