
#$ Procedural Language
a=1
print(a)

#$ Procedural Language
def sqr(x):
    return x*x

print(sqr(5))

class Person: 
    def sayHello(self):
        print("Hello")

p = Person()
p.sayHello()

#* This is runtime

try: 
    p.sayBye()
except:
    print("Not there")