class Parent:
    x = 'X'


class Child(Parent):
    y = 'Y'


p = Parent()
print(p.x)

ch = Child()
print(ch.x)
print(ch.y)
