class Student:
    profession = 'Developer'

    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print('init')


stud1 = Student('Dima', 'Sol', 2)
