
class Person:
    def __init__(self, id, name):
        #! this is name Mandling hides the variable and outer code cant access
        self.__id = id
        self.__name = name

    #! Get the proerty created with name mandling
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(Self, value):
        if value<1:
            raise AttributeError("id {value} cannot be less than one")
        Self.__id = value


p = Person(1 , 'John')
print(p.id)

p.id = 0
# print(p.id) 
