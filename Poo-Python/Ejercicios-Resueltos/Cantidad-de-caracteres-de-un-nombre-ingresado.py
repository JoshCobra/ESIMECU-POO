#Programa carga el nombre de una persona, muestra el primer caracter del nombre y la cantidad de letras que lo componen
#mostrar un mensaje si comienza por vocal

nombre = input("Introduce el nombre de una persona: ")

inicial = nombre[0]
longitud = len(nombre)

print("La inicial del nombre: ", inicial)
print("Longitud del nombre: ", longitud)


if inicial.upper() in 'AEIOU':
    print("El nombre inicia con una vocal")
