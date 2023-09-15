class Student:
    profession = 'Developer'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def check_profession(self):
        print(self.profession)

    @staticmethod
    def print_location():
        print('Санкт-Петербург')


new_student = Student('Dima', 'Sol', 2)

print(new_student.profession)
print(new_student.first_name)
print(new_student.last_name)
print(new_student.age)

new_student.check_profession()
new_student.print_location()
