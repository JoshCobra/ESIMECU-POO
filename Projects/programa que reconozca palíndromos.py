'''
Realiza un programa que reconozca palíndromos (es decir, 
palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es palíndromo ("radar") tendría que devolver True.'''
#DE LA ROSA VAZQUEZ JOSUE

a=1
while a==1:

    palabra= input("Introduce una Palabra: ").lower()

    es_palindromo = palabra == palabra[::-1]
    #La expresión palabra[::-1] invierte la palabra 
    #https://docs.python.org/es/3/reference/expressions.html

    print(es_palindromo)
    a=int(input("Desea Introducir otra Palabra? si=1/no=2: "))

else:
    print("Programa Terminado")


