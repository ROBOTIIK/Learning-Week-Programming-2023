class Details:
    def __init__(self, name="<no name>", id_number="<no id>"):
        self.__name = name
        self.__id_number = id_number
    def setData(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
    def name(self):
        return self.__name
    def id_number(self):
        return self.__id_number
    

class Student(Details):
    def __init__(self, name, id_number, courses):
        super().__init__(name, id_number)
        self.__courses = courses
    def courses(self):
        return self.__courses

class Professor(Details):
    def __init__(self, name, id_number, courses_taught):
        super().__init__(name, id_number)
        self.__courses_taught = courses_taught
    def courses_taught(self):
        return self.__courses_taught

def main():
    s = Student("Alice", 1234, ["Introduction to Computer Science", "Data Structures"])
    p = Professor("Bob", 5678, ["Database Systems", "Web Development"])
    print(s.name(), s.id_number(), s.courses())
    print(p.name(), p.id_number(), p.courses_taught())

if __name__ == "__main__":
    main()