class Apple:
    stages = ['blossom', 'green', 'red']

    def __init__(self, Id):
        self.Id = Id
        self.stage = self.stages[0]

    def grow(self):
        if self.stage != self.stages[-1]:
            stage_index = self.stages.index(self.stage)
            self.stage = self.stages[stage_index + 1]
        else:
            print('apple ' + str(self.Id) + ' red already')

    def isRipe(self):
        if self.stage == self.stages[-1]:
            return True
        else:
            return False


class Tree:
    def __init__(self, *apples):
        self.apples = apples

    def grow(self):
        for apple in self.apples:
            apple.grow()

    def allIsRipe(self):
        for apple in self.apples:
            if not apple.isRipe():
                return False
        return True

    def harvest(self):
        self.apples = []
        print('harvest is done!')


class Gardener:
    def __init__(self, name, *trees):
        self.name = name
        self.trees = trees

    def work(self):
        for tree in self.trees:
            tree.grow()

    def harvest(self):
        for tree in self.trees:
            if tree.allIsRipe():
                tree.harvest()
            else:
                print('too early for harvest!')


a1 = Apple(1)
a2 = Apple(2)
a3 = Apple(3)
a4 = Apple(4)
a5 = Apple(5)
t1 = Tree(a1, a2, a3, a4, a5)
print(t1.apples)

a1.grow()
for a in t1.apples:
    print(a.stage)
print(t1.allIsRipe())

g1 = Gardener('Steve', t1)
g1.work()
g1.harvest()
g1.work()
g1.harvest()

print(t1.apples)
