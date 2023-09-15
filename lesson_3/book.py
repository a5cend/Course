class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False


    def check_out(self):
        if self.checked_out:
            print('Книга находится у абонента')
        else:
            print('Выдаем книгу абоненту')
            self.checked_out = True

    def check_in(self):
        if self.checked_out:
            print('Принимаем книгу в библиотеку')
            self.checked_out = False
        else:
            print('Книга в наличии')


myBook = Book('BlindSight', 'P.Watts')
myBook.check_out()
myBook.check_out()
myBook.check_in()
myBook.check_in()
