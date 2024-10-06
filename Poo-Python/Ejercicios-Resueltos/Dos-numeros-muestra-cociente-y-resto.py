
# Programa que pide dos numeros enteros y muestra el cociente y el resto

n = int(input("Introduce el primer numero (n): "))
m = int(input("Introduce el segundo numero (m): "))

cociente = n // m
resto = n % m

print(n,"entre",m, "da un cociente",cociente, "y un resto",resto)
