
#~ generator magic - state machine
# def fn():
#     #? state = 1
#     yield 1
#     #? state = 2
#     yield 2
#     #? state = 3
#     yield 3 
#     #? state = 4
#     yield 4     

# for num in fn():
#     print(num)


# def fn1():
#     for num in range(1,100):
#         yield num

# for num in fn1():
#     print(num)


def primeNumbers(start=0, end=11):
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):      
                if num%i == 0:
                    break
            else:
                # print(num)
                yield num
                # break

for prime in primeNumbers(10,31):
    print(prime)


# primeNumbers(11, 25);
