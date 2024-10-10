# Introducción a la Sintaxis Básica de C++ y sus Diferencias con C

C++ es _casi_ un superconjunto de C y comparte su sintaxis básica para las
declaraciones de variables, tipos primitivos y funciones.

### Punto de entrada del programa en C++
Al igual que en C, el punto de entrada de tu programa en C++ es la función main, que tiene un retorno de tipo entero. Este valor actúa como el código de salida del programa.

```
int main(int argc, char** argv)
{
    // Los argumentos de la línea de comandos se pasan por argc y argv, igual que en C.
    // argc: número de argumentos.
    // argv: un arreglo de strings de estilo C (char*) que representan los argumentos.
    // El primer argumento es el nombre con el que el programa es llamado.

    // Puedes omitir argc y argv si no te interesan los argumentos.
    // Esto deja la definición de la función como: int main ()

    // El retorno de 0 indica que el programa ha finalizado con éxito.
    return 0;
}
```

### Diferencias clave entre C++ y C:

1. Literal de caracteres
En C++, un carácter literal es del tipo char, mientras que en C es del tipo int.
```
// En C++
sizeof('c') == sizeof(char) == 1
// En C
sizeof('c') == sizeof(int)
```

### 2. Prototipado estricto en C++
C++ requiere un prototipado estricto de las funciones. Esto significa que una función sin argumentos debe declararse de forma explícita.
```
// En C++
void func();  // Función que no acepta argumentos
// En C
void func();  // Función que podría aceptar cualquier número de argumentos
```

### 3. Uso de nullptr en lugar de NULL
En C++, se prefiere nullptr en lugar de NULL para representar un puntero nulo.
```
int* ip = nullptr;
```

### 4. Cabeceras estándar de C en C++
Las cabeceras de C estándar están disponibles en C++, pero se les ha dado el prefijo 'c' y no llevan el sufijo .h. Por ejemplo:
```
#include <cstdio>
```
Ejemplo completo en C++
Aquí un programa simple que imprime "Hola mundo" en C++ usando la función printf:

```
int main()
{
    printf("Hola mundo!\n");
    return 0;
}
```



Fuente: https://learnxinyminutes.com/docs/c++/

