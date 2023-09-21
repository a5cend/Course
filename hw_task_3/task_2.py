class Student:

    def __init__(self):
        self.knowledge = []

    def take(self, material: str):
        self.knowledge.append(material)


class Teacher:

    def __init__(self):
        self.number_students = 0

    def teach(self, material: str, *students):
        for student in students:
            student.take(material)
            self.number_students += 1


class Material:

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.list = []
        for arg in args:
            self.list.append(arg)


materials = Material('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
print('materials.list =', materials.list)

t1 = Teacher()
s1, s2, s3, s4 = Student(), Student(), Student(), Student()

t1.teach(materials.list[0], s1, s2)
t1.teach(materials.list[1], s2, s3)
t1.teach(materials.list[2], s3, s4)
t1.teach(materials.list[3], s1, s3)
t1.teach(materials.list[4], s2, s3)

for s in [s1, s2, s3, s4]:
    print(s.knowledge)
