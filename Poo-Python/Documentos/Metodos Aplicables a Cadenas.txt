'''Métodos Aplicables a Cadenas

capitalize() devuelve una copia de la cadena con la primera letra en Mayúscula

center() devuelve una copia de la cadena centrada y con longitud n

find(sub,{desde{,hasta}}) devuelve la posición de la primera aparición de sub
en la cadena, si se inlcude desde, la busqueda comienza en esa posicion y
termina en, hasta, si se especifica.

isalnum() devuelve cierto si la cadena es no vacia y solo contiene letras
y digitos

isalpha() devuelve cierto si la cadena es no vacia y solo contiene letras

isdigit() devuelve cierto si la cadena es no vacia y solo contiede digitos

islower() devuelve cierto si todas las letras de la cadena son minusculas
y al menos una minuscula

isspace() devuelve cierto si la cadena es no vacia y todos los caracteres
son espacio

isupper() devuelve cierto si todas las letras de la cadena son mayusculas
y hay al menos una mayuscula

lower() devuelve una copia de la cadena en minusculas

upper() devuelve una copia de la cadena en mayusculas

lstrip() devuelve una copia de la cadena con blancos iniciales omitidos

replace(v, n) devuelve una copia de la cadena donde se han sustituido
todas las apariciones de v con n'''

n = input('Diga una cadena para aplicar los metodos: ')

print("Su cadena con Metodo capitalize()")
print(n.capitalize())

print("Su cadena con Metodo center()")
print(n.center(40))

print("Su cadena con Metodo Find()")
print(n.find('a'))

print("Su cadena con Metodo isalnum()")
print(n.isalnum())

print("Su cadena con Metodo isalpha()")
print(n.isalpha())

print("Su cadena con Metodo islower()")
print(n.islower())

print("Su cadena con Metodo isupper()")
print(n.isupper())

print("Su cadena con Metodo lower()")
print(n.lower())

print("Su cadena con Metodo upper()")
print(n.upper())

print("Su cadena con Metodo lstrip()")
print(n.lstrip())

print("Su cadena con Metodo replace(), reemplazara las a con o")
print(n.replace('a', 'o'))




