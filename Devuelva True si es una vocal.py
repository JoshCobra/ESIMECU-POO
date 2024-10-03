#Realiza un programa que tome un carácter y devuelva True si es una vocal, 
# de lo contrario devuelve False
#DE LA ROSA VAZQUEZ JOSUE

a=1
while a==1:

    caracter = input("Introduce un Caracter: ").lower()

    es_vocal = caracter in 'aeiou'

    print(es_vocal)
    a=int(input("Desea Introducir otro Caracter? si=1/no=2: "))

else:
    print("Programa Terminado")
