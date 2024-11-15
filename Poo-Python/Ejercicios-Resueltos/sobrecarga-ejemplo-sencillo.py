a = 50
b = 45

print(a+b)

a = "lizette"
b = "Carolina"

print(a+b)

class libro:
    def __init__(self, paginas):
        self.paginas = paginas

    def __add__(self, otro):
        return self.paginas + otro.paginas

    
a1 = libro(500)
a2 = libro(300)

print(a1+a2)