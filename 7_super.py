class Base:
    def __init__(self):
        print('Base init')

b =Base()

class Child:
    def __init__(self):
        super().__init__()
        print('Derived class')

child = Child()