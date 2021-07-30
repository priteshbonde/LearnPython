import antigravity
#! List Brackets[]

list =[10, 1,2,3,4,5]
print(list, type(list), list.count)
list.append(13)
print('Updated list', list.count)
list.sort()
print('sorted List', list)

#? removes specific items
list.remove(10)
print('Item removed', list)

#? removes items on the index
poppedItem = list.pop(3)
print('Popped Item', poppedItem, list)

#! tuple Parenthesis ()

tuple =(1,1,2,3,5,3,4,'Some String')
print(tuple, type(tuple))

#? Not allowed
#  tuple[tuple.count] = 100
# print('updated Tuple', tuple)
#! set Braces{}

set = {1,1,2,5,4,1,3,'Some string'}
print(set, type(set))

set.add(35)
print('Added in set', set)

set.remove(1)
print('updated Set', set)

#! Dictionary Braces{}

dict = {'id': 1, 'name':'John Doe'}
print(dict, type(dict))

dict.update([("professsion", "Cook")])
print(dict)
poppedDict = dict.pop('id')
print(poppedDict, dict)


# def fun1():
#     print('test 1')
#     print('add one line')
#   fun1()
