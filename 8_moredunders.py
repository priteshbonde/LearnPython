class Number:
    def __init__(self, value):
        self.value = value

    #~ Operation overloading
    def __gt__(lhs, rhs):
        return lhs > rhs

    def __eq__(lhs, rhs) -> bool:
        return lhs.value == rhs.value


n1 = Number(10)
n2 = Number(15)

print(n2 >n1)