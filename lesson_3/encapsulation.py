class Encapsulation:
    def __init__(self):
        self.open_param = {'db_name': 'student', 'port': '5768'}
        self.__config = {'db_name': 'student', 'db_pass': 'hgjduv'}


obj1 = Encapsulation()

print(obj1.open_param)

# print(obj1.__config)
# AttributeError: 'Encapsulation' object has no attribute '__config'

print(obj1._Encapsulation__config)
