### Para apoyarte a resolver los ejercicios checa:
[DOCUMENTOS](Documentos)
 - [Que es Poo en Python](/Poo-Python/Python-POO.md)
 - [Tipos De Datos Y Operadores](Documentos/Tipos-de-datos-Primitivos-y-Operadores.md)
 - [Variables Y Colecciones](Documentos/Variables-y-Colecciones.txt)
 - [Manejo De Cadenas De Texto](Documentos/Manejo-Cadenas-de-Texto.md)
 - [Metodos Aplicables a Cadenas](Documentos/Metodos-Aplicables-a-Cadenas.txt)
    1. [Ejemplo Operaciones Con Cadenas](Documentos/OperacionesConCadenas.PNG)

# LISTA DE EJERCICIOS

1. Escribir un programa que **solicite por teclado 10 notas de alumnos y nos informe cuantos tienen notas mayores o iguales a 7** y cuantos menores.

2. Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere **calcular de forma automática el precio que debe cobrar a sus clientes por entrar.** El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

3. Realiza un **programa que tome como argumento dos o tres números y devuelva el mayor de ellos.**

4. Realiza un programa que **calcule la longitud de una cadena dada.**  

5. Realiza un programa que tome un carácter y **devuelva True si es una vocal, de lo contrario devuelve False.** 

6. Realiza un **programa que reconozca palíndromos** (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es palíndromo ("radar") tendría que devolver True. 

7. Realizar un **programa que reciba una palabra y cuente** cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar **todas las vocales.** Que el usuario sea quien elija la palabra. 

8. Realizar un programa, en el cual plasmes al menos **6 metodos de las que existen en python**, se incluye un archivo para tu facil acceso en: `/ESIMECU-POO/Poo-Python/Documentos/Metodos-Aplicables-a-Cadenas.txt` o [Metodos Aplicables a Cadenas](Documentos/Metodos-Aplicables-a-Cadenas.txt)

9. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un **programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.** 

10. Escribir un programa que **pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.** 

11. Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido. 

12. Escribir un programa que **solicite por teclado 10 notas de alumnos** y nos informe cuántos tienen **notas mayores o iguales a 7 y cuántos menores**
Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen, mostrar un mensaje si comienza con vocal dicho nombre
Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".
Se cuenta con la siguiente información:
 - Las edades de 5 estudiantes del turno mañana.
 - Las edades de 6 estudiantes del turno tarde.
 - Las edades de 11 estudiantes del turno noche.
 - Las edades de cada estudiante deben ingresarse por teclado.
 - a) Obtener el promedio de las edades de cada turno (tres promedios)
 - b) Imprimir dichos promedios (promedio de cada turno)
 - c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio de edades mayor.

13. Escriba un programa que permita crear una lista de palabras, y realice las siguientes accciones utilizando un menu:
 - El programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista
 - El programa tiene que imprimier la lista. 
 - El programa pida una palabra y diga cuántas veces aparece esa palabra en la lista. 
 - El programa pida dos palabras y sustituya la primera por la segunda en la lista. 
 - El programa pida una palabra y elimine esa palabra de la lista. 
 - El programa elimine las palabras diplicadas de la lista. 
 - Salir

14. Realiza un programa de una Agenda, utilizando lista de listas de listas de listas, en donde se deberá seleccionar:
 - Año
 - Mes
 - Dia 
 - Hora
 - Información del evento que se agendo.
 - Se podrán registrar "n" numero de eventos.

16. Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar. 
Para representar una pila vamos a utilizar una lista de cadenas de caracteres. 
Vamos a crear varias funciones para trabajar con la pila: 
 - **LongitudPila:** Función que recibe una pila y devuelve el número de elementos que tiene. 
 - **EstaVaciaPila:** Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos. 
 - **EstaLlenaPila:** Función que recibe una pila y que devuelve si la pila está llena. 
 - **AddPila:** función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error. 
 - **SacarDeLaPila:** Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error. 
 - **EscribirPila:** Función que recibe una pila y muestra en pantalla los elementos de la pila. 
 - Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones: 
    1. Añadir elemento a la pila 
    2. Sacar elemento de la pila 
    3. Longitud de la pila 
    4. Mostrar pila 
    5. Salir 


17. Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
- Finalizar al ingresar el número 0, el cual no debe guardarse.
A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
- Recorrer la lista para imprimir la sumatoria de todos los elementos.
- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
