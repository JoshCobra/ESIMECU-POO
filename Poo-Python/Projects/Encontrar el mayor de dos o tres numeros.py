#Programa que tome como argumento dos o tres números y devuelva el mayor de ellos
#DE LA ROSA VAZQUEZ JOSUE

n=1
while n==1:

    num1 = float(input("Introduce Primer Numero: "))
    num2 = float(input("Introduce un Segundo Numero: "))

    opcion = input("Quieres introducir un tercer Numero? (s/n): ")

    if opcion.lower() == 's':
        num3 = float(input("Introduce el Tercer Numero: "))
        mayor = max(num1, num2, num3)
#La funcion max() identifica y retorna el valor mas alto
    else:
        mayor = max(num1, num2)
    print(f"El Numero Mayor es: {mayor}")

    n = int(input("Volver a Ingresar? si=1/no=otro:"))
else:
    print("Programa Terminado")
