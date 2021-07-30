def header_count(num=10): #$ this is getting 80
    def header(fn): #$ this is getting report
        def deco(*args, **kwds): #this is getting 2020 q4
            print("-"*num)
            fn(*args, **kwds)
            print("-"*num)
        return deco
    return header

@header_count(10)
def func():
    print("func")

@header_count(20)
def report(year, qtr):
    print(f"Annual report {year} {qtr}")


report(2020, 'Q4')
func()