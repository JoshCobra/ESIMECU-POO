
# Programa que pregunta cantidad a invertir, interes anual y años
#DE LA ROSA VAZQUEZ JOSUE

cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interes anual (%): "))
años = float(input("Introduce el numero de años: "))

capital = cantidad * (1 + interes / 100) ** años

print("El capital obtenido tras", años, "años es:" ,capital)
