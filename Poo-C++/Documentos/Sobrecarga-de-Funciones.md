# Sobrecarga de Funciones en C++
La sobrecarga de funciones es una característica que permite a C++ definir múltiples funciones con el mismo nombre, 
siempre que sus parámetros sean diferentes en tipo o número.

### Definición de la sobrecarga de funcione
```
// C++ soporta sobrecarga de funciones
// siempre que cada función tenga diferentes parámetros.
```
Ejemplo de funciones sobrecargadas
En este ejemplo, tenemos dos versiones de la función print. Una acepta un char* (cadena de caracteres), mientras que la otra acepta un int.
```
void print(char const* myString)
{
    printf("String %s\n", myString);
}

void print(int myInt)
{
    printf("Mi entero es %d", myInt);
}
```

### Uso de las funciones sobrecargadas
Dependiendo del tipo de argumento que se le pase a la función print, se llamará a la versión adecuada de la función:
```
int main()
{
    print("Hello");  // Corresponde a void print(const char*)
    print(15);       // Corresponde a void print(int)
}
```

Explicación:

    - print("Hello"): Llama a la función que acepta un const char* y muestra una cadena de caracteres.
    - print(15): Llama a la función que acepta un entero y muestra su valor.



Fuente: https://learnxinyminutes.com/docs/c++/
