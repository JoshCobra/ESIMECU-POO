# Argumentos de Función por Defecto en C++
En C++, es posible proporcionar valores por defecto para los argumentos de una función,
lo que significa que si no se pasan ciertos argumentos al llamar a la función, se utilizarán los valores predeterminados.

### Definición de una función con argumentos por defecto
```
// Puedes proporcionar argumentos por defecto para una función si no son proporcionados por quien la llama.

void doSomethingWithInts(int a = 1, int b = 4)
{
    // Hacer algo con los enteros aquí
}
```
En la función `doSomethingWithInts`, los argumentos `a` y `b` tienen valores predeterminados. 
Si no se pasan argumentos al llamar a la función, a tomará el valor de 1 y b el valor de 4.

### Llamadas a la función con y sin argumentos
```
int main()
{
    doSomethingWithInts();      // a = 1,  b = 4
    doSomethingWithInts(20);    // a = 20, b = 4
    doSomethingWithInts(20, 5); // a = 20, b = 5
}
```
Explicación:

`doSomethingWithInts():` Como no se proporcionan argumentos, se utilizan los valores predeterminados, a = 1 y b = 4.

`doSomethingWithInts(20):` Solo se proporciona un argumento, por lo que a = 20 y b toma su valor predeterminado, b = 4.

`doSomethingWithInts(20, 5):` Se proporcionan ambos argumentos, por lo que a = 20 y b = 5.

### Restricciones en los argumentos por defecto
```
// Los argumentos predeterminados deben estar al final de la lista de argumentos.

void invalidDeclaration(int a = 1, int b) // Error!
{
}
```
Los argumentos con valores predeterminados siempre deben estar al final de la lista de argumentos. 
El ejemplo anterior muestra un error porque b no tiene un valor predeterminado, pero está después de a, que sí lo tiene.



*Fuente: https://learnxinyminutes.com/docs/c++/*

