#Realiza un programa que calcule la longitud de una cadena dada
#DE LA ROSA VAZQUEZ JOSUE

c=1
while c==1:

    cadena = input("Ingresa la Cadena Para Calcular su Longitud: ")

    len(cadena)
#La funcion len() calcula la longitud del string
#https://docs.python.org/es/3/library/functions.html#len

    print("La Cadena tiene:",len(cadena),"Caracteres")
    c = int(input("Desea Agregar Otra Cadena? si=1/otro=no: "))

else:
    print("Programa Terminado")
