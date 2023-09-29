import random


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
        self.apples = list(apples)
        self.age = 1

    def grow(self):
        for apple in self.apples:
            apple.grow()
        if 2 < self.age < 6 and random.randint(0, 10) > 1:
            new_apple = Apple(len(self.apples) + 1)
            self.apples.append(new_apple)
            print('random new apple!')
        self.age += 1

    def allIsRipe(self):
        for apple in self.apples:
            if not apple.isRipe():
                return False
        return True

    def harvest(self):
        removed_apples = 0
        for apple in self.apples:
            if apple.isRipe():
                self.apples.remove(apple)
                removed_apples += 1
        if removed_apples > 0:
            print(f'harvest is done!, removed apples = {removed_apples}')
        else:
            print(f'too early for harvesting!')


class Gardener:
    def __init__(self, name, *trees):
        self.name = name
        self.trees = trees

    def work(self):
        for tree in self.trees:
            print('working...')
            tree.grow()

    def harvest(self):
        for tree in self.trees:
            print('harvesting...')
            tree.harvest()

    def stat(self):
        # print('len(self.trees) = ', len(self.trees))
        for tree in self.trees:
            print('age = ', tree.age)
            print(f'{len(tree.apples)} apples')
            for apple in tree.apples:
                print(f'id {apple.Id}, {apple.stage}')


t1 = Tree()
g1 = Gardener('Steve', t1)

count = 0
while not (len(t1.apples) == 0 and count > 7):
    g1.stat()
    g1.harvest()
    g1.work()
    print('\n')
    count += 1

print(f'Все яблоки собраны, циклов {count}')

