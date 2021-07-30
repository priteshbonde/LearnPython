class Person:
    pass

    class Address:
        def __init__(self, addr, city, state, zip):
            pass

    def __init__(self, name, addr, city, state, zip):
        self. name = name
        self.address = Person.Address(addr, city, state, zip)


# per = Person()

#! function cannot access another function's stackframe


def Outer():
    a =1 #$ Local variable for outer

    def Inner(): #! Inner Function
        b = 2
        print(f"b = {b} and a = {a}")
    
    Inner()

Outer()