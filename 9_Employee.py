class Employee:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, value):
         if value<1:
            raise AttributeError("id {value} cannot be less than one")
         self.__id = value

    id= property(get_id, set_id) #! in this case no need for decorator


e = Employee(1 , "Ron")
e.id = 5
print(e.id)