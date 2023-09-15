class Data:
    def __new__(cls, *args, **kwargs):
        print('state fetching')
        return super().__new__(cls)

    def __init__(self, array):
        self.array = array
        print(f'data processing: {self.array}')


d1 = Data([1])
d2 = Data([2, 3])
