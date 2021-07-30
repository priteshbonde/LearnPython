# from helloworld import sayHi


class Person:

    def __init__(self, salary, name):
        salary = salary
        name = name


    common = "This is common"
    def sayHello(self, name):
        print("Hello " + name)

Person.AgainCommon = "This is one more common"

sanketObj = Person(100000, "Sanket")
sanketObj.java = True
print('Sanket object Location', id(sanketObj))
print('Person Java', sanketObj.java)
print('Common vars for sanket', sanketObj.common, sanketObj.AgainCommon)
print(sanketObj.sayHello('Sanket'))


amitObj = Person(1000000, "Amit")
amitObj.Qa = True
print('Amit object Location', id(amitObj))
print('Amit QA', amitObj.Qa)
print('Common vars amit', sanketObj.common, sanketObj.AgainCommon)
print(sanketObj.sayHello('Amit'))

#! This line throws error as Amit java is not there
# print('Amit Java', amitObj.java)


