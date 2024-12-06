class Contador:
    def __init__(self, min,seg):
        self.min = min
        self.seg = seg

    def __str__(self):
        return f" Minutos: {self.min} Segundos: {self.seg}"
    
    def __add__(self, other):
        minutos = self.min + other.min
        segundos = self.seg + other.seg
        return f" Hora Final {minutos} : {segundos}"

    def __radd__(self, other):
        return self.__add__(other)
    

hora1 = Contador(12,54)
hora2 = Contador(5,6)
print(hora1)
print(hora2)

hora_final = hora1 + hora2

print(hora_final)