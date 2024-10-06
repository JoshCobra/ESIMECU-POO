#Escribir un programa que solicite por teclado 10 notas de allumnos y nos informe cuantos tienen notas mayores 
# o iguales a 7 y cuantos menores

notas_mayores = 0
notas_menores = 0

for i in range(10):
    nota =  float(input("Introduce la nota del alumno: "))
    i+1
    if nota >= 7:
        notas_mayores += 1
    else:
        notas_menores += 1

print("Las notas Mayores a 7 son: ", notas_mayores)
print("Las notas Menores a 7 son: ", notas_menores)
