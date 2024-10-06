#Programa Convierte de Binario a Decimal

n=1
while n == 1:
    binario= input("Ingrese numero binario: ")
    entero=int(binario, 2)
    print("El Numero Entero es: ",entero)
    
    n = int(input("Desea Agregar otro numero 1=si:"))
else:
    print("Programa Terminado")

#Programa Convierte de Decimal a Binario

decimal = int(input("Ingrese un numero decimal: "))
binario=bin(decimal)
print("El Numero Binario es: ",binario )
