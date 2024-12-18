class BooleanoPersonalizado:
    def __init__(self, valor):
        self.valor = bool(valor)
    
    def __and__(self, otro):
        return BooleanoPersonalizado(self.valor and otro.valor)
    
    def __or__(self, otro):
        return BooleanoPersonalizado(self.valor or otro.valor)
    
    def __repr__(self):
        return str(self.valor)

# Uso
a = BooleanoPersonalizado(True)
b = BooleanoPersonalizado(False)

print(a & b)  # False (simula `and`)
print(a | b)  # True (simula `or`)
