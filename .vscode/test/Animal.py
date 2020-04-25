class Animal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + ' walks.')
        print(self.name + ' walks.')


duck = Animal('Duck')
duck.walk()
