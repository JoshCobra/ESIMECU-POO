#Ejercicio 17

numeros = []
while True:
    numero = int(input("Ingrese un número (con 0 termina el ingreso de números): "))
    if numero == 0:
        break
    numeros.append(numero) #Función append()


numero_eliminar = int(input("Ingrese un número para eliminar su primera ocurrencia: "))
def bucle_eliminar(numeros, numero_eliminar):
    if numero_eliminar in numeros:
        numeros.remove(numero_eliminar)
        print("Numero eliminado correctamente")
    else:
        print("Numero no se encuentra en la lista")
        numero_eliminar = int(input("Ingrese otro número: "))
        bucle_eliminar(numeros, numero_eliminar)

bucle_eliminar(numeros, numero_eliminar)

'''
numero_eliminar = int(input("Ingrese un número para eliminar su primera ocurrencia: "))
for numero_eliminar in numeros:
    numeros.remove(numero_eliminar) #Función remove()
    print(f"El número {numero_eliminar} ha sido eliminado de la lista.")
else:
    print(f"No se puede eliminar el número {numero_eliminar} porque no está en la lista")
'''


sumatoria = sum(numeros) #Función sum()
print(f"La sumatoria de los números en la lista es: {sumatoria}")


numero_limite = int(input("Ingrese un número límite: ")) 
lista_menores = [n for n in numeros if n < numero_limite] 
# [n for n in numeros if n < numero_limite] Comprensión de listas en python, 
# itera a través de cada elemento "n" en la lista "numeros"
# for n in numeros significa que estamos recorriendo cada numero dentro de la lista
print(f"Los números menores que {numero_limite} son: {lista_menores}")

contador_numeros = []
for numero in set(numeros):  #Función set(), esta función evita que se cuente mas de una vez el mismo numero
    contador_numeros.append((numero, numeros.count(numero)))

print("Lista de tuplas con números y su cantidad de ocurrencias: ")
print(contador_numeros)