'''Realizar un programa que reciba una palabra y cuente cuantas letras "a" tiene, 
cuantas letras "e" tiene y así hasta completar todas las vocales. 
Que el usuario sea quien elija la palabra. '''
#DE LA ROSA VAZQUEZ JOSUE

n=1 
while n==1:

    palabra = input("Introduce una palabra: ").lower()


    a = palabra.count('a')
    e = palabra.count('e')
    i = palabra.count('i')
    o = palabra.count('o')
    u = palabra.count('u')
#El metodo count() retorna el numero de ocurrencias del valor solicitado
#https://docs.python.org/es/3/library/array.html#array.array.count


    print("La vocal 'a' aparece", a, "veces")
    print("La vocal 'e' aparece", e, "veces")
    print("La vocal 'i' aparece", i, "veces")
    print("La vocal 'o' aparece", o, "veces")
    print("La vocal 'u' aparece", u, "veces")

    n=int(input("Desea Introducir Otra Palabra? si=1/no=2: "))
else:
    print("Programa Terminado")