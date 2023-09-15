class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'соединение с БД: [{self.user}] [{self.password}] [{self.port}]')

    @staticmethod
    def close():
        print('закрытие соединения с БД')


db = DataBase('login123', 'PaSsWoRd', '8375')
db2 = DataBase('login456', 'wOrDpAsS', '6503')

print(id(db), id(db2))
db.connect()
db2.connect()

db.close()
