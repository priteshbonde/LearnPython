import dis

#! Everything is Object

a=5

b=a

print(a)
print(id(a))

print(b)
print(id(b))

def add(a,b):
    print('b',id(b))
    c=a+b
    return c

print(add(10,5))
print(id(add))

dis.dis(add)