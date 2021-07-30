def fn():
    print("in extern")

class Person:
    def __init__(this, id, name): #! First parameter is not can be anything no need to have self but as per convention keep it self
        this.id = id
        this.name = name

    def print(me):
        print(me.id, me.name)

    def __del__(self): #! invoked when object is deleted(ref count -> 0)
        print("Goodbye")

    def __delattr__(self, name: str): #! Intercept Delete specific attribute
        print(f" trying to delete {name}")
        # raise AttributeError(f"cannot delete {name}")

    def __delete__(self, instance):
        print(" Part of another class")

    def __getattr_(self, attr): #! interceptor when someone try to retrieve the attribute
        print(f"someone looking for attibute {attr}")
        return self[attr]

    def __setattr__(self, name: str, value: Any): #! interceptor when someone try to assign the attribute
        if name[0:6] == "_priv_":
            raise AttributeError("Cant set private variables.")

class Company:
    ceo1 = Person(3, "ross")
    def __init__(self):
        self.ceo = Person(2 , "Tim")

p = Person(1, "Guido")
q = p
del p.id #! Does not destroys the object, it reduces the ref count and Delete dunder does not get called after this
q.extern = fn
q.print()  
q.extern()
del q.extern #! function can also be deleted

comp = Company()
del comp.ceo.id
del comp.ceo1

print(q.id)

        