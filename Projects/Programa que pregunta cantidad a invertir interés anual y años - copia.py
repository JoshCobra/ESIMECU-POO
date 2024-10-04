
c = float(input("Cual es la cantidad a Invertir: "))
interes = float(input("Cual es el interes anual: "))
anio = float(input("Cuantos años a invertir: "))

total = c * (1 + interes / 100) ** anio

print("El capital obtenido tras", anio, "años es:" ,total)
