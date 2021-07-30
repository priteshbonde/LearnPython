
#! this function can act as a decorator. 
def hello(fn):
    print("in hello")
    return fn


@hello
def greeting():
    print("Greet")


greeting()

def header(fn):
    print('-','*80')
    return fn

@header
def report():
    print("Sales report")

report()


def security(fn):
    if user != 'Admin':
        raise AttributeError("You are not allowed to access the secure method")

user = "user"

@security
def someSecurResource():
    print("This is secure")

someSecurResource()