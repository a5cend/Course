import random


class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Human):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.knowledge = []

    def take(self, material: str):
        self.knowledge.append(material)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        self.knowledge.remove(self.knowledge[random.randint(0, len(self.knowledge) - 1)])


class Teacher(Human):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.number_students = 0

    def teach(self, material: str, *students):
        for student in students:
            student.take(material)
            self.number_students += 1


class Material:

    def __init__(self, *args, **kwargs):
        self.list = []
        for arg in args:
            self.list.append(arg)

    def __len__(self):
        return len(self.list)


materials = Material('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
print('materials.list =', materials.list)

t1 = Teacher(name='Tamara Vasilyevna', age=35, gender='woman')
s1 = Student(name='Dima', age=20, gender='man')
s2 = Student(name='Vanya', age=21, gender='man')
s3 = Student(name='Dasha', age=22, gender='woman')
s4 = Student(name='Olya', age=23, gender='woman')

t1.teach(materials.list[0], s1, s2)
t1.teach(materials.list[1], s2, s3)
t1.teach(materials.list[2], s3, s4)
t1.teach(materials.list[3], s1, s3)
t1.teach(materials.list[4], s2, s3)

for s in [s1, s2, s3, s4]:
    print(s.knowledge)

print('len(materials) =', len(materials))
print('len(s1) =', len(s1))
print('len(s2) =', len(s2))
print('len(s3) =', len(s3))
print('len(s4) =', len(s4))

for s in [s1, s2, s3, s4]:
    s.forget()
    print(s.knowledge)
