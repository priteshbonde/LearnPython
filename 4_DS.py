
import this

#! Stupid
numbers =[1, 2,3,4,5,6,7,8,9,10]

#! Idiot

value = range(1,11)
print("normal range", value)



numberList = [value for value in range(1,11)]
print('Number added using comprehension', numberList)

#? add 1 to 10 to existing without manually writing or for loop
someList = [55]
someList.extend( range(1,11))
# numbers.copy(numberList)

# numberList = [numbers, x for x in numbers if x > 5 ]
print("Final Output: Extended List", someList)