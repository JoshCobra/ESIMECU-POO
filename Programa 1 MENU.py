#Indicar Bisiesto o No Bisiesto

n = int(input("quieres continuar 1=si:"))
while n == 1:
    anio = int(input("introduce el año:" ))
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print("Es Bisiesto")
    else:
        print("No es Bisiesto")
    n = int(input("quieres volver a continuar 1=si/otro=no:"))
else:
    print("programa 1 terminado")
    
	
#Ingresa un numero entero de horas y convierte a horas y minutos

s = int(input("quieres continuar 1=si:"))
while s == 1:

    num = int(input("introduce el numero:"))
    horas = num // 60
    minutos = num % 60

    print("horas:")
    print(horas)
    print("minutos:")
    print(minutos)

    n = int(input("quieres volver a continuar 1=si/otro=no:"))
else:
    if n != 1:
        print("programa terminado")
