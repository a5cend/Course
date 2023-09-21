class Rect:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def square(self):
        return self.width * self.heigth

    def perimeter(self):
        return (self.width + self.heigth) * 2


r = Rect(2, 4)
print(r.square())
print(r.perimeter())
