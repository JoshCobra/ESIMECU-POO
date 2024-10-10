# Introduccion a los Tipos de Datos Primitivos Y Operadores en Python

Los comentarios de una sola línea empiezan con el símbolo "#".
""" Las cadenas de texto de varias líneas se pueden escribir usando tres comillas dobles y se utilizan a menudo para documentación. """

### Puedes trabajar con números
```
3 # => 3
```

### Las operaciones matemáticas son lo que esperas
```
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 5 # => 7.0
```

### La división entera redondea hacia abajo (infinito negativo)
```
5 // 3 # => 1
-5 // 3 # => -2
5.0 // 3.0 # => 1.0
# también funciona con decimales -5.0 // 3.0 # => -2.0
```

### El resultado de la división siempre es un número decimal
```
10.0 / 3 # => 3.3333333333333335
```
### Operación de módulo (resto de la división)
```
7 % 3 # => 1
```
### `i % j` tiene el mismo signo que `j`, a diferencia de otros lenguajes como C
```
-7 % 3 # => 2
```

### Exponentes ("x**y", x elevado a la potencia de y)
```
2**3 # => 8
```
### Puedes usar paréntesis para cambiar el orden de las operaciones
```
1 + 3 * 2 # => 7
(1 + 3) * 2 # => 8
```

### Los valores booleanos (verdadero/falso) son tipos de datos básicos
```
True # => True
False # => False
```
### Se niegan con "not"
```
not True # => False
not False # => True
```

# Operadores lógicos
Nota: "and" y "or" son sensibles a mayúsculas
True and False # => False False or True # => True

True y False son en realidad números (1 y 0) pero tienen palabras clave diferentes
True + True # => 2 True * 8 # => 8 False - 5 # => -5

Los operadores de comparación también interpretan True y False como números
0 == False # => True 2 > True # => True 2 == True # => False -5 != False # => True

Algunos valores siempre se consideran False: None, 0, y listas/cadenas/diccionarios vacíos.
Los demás valores se consideran True.
bool(0) # => False bool("") # => False bool([]) # => False bool({}) # => False bool(()) # => False bool(set()) # => False bool(4) # => True bool(-6) # => True

Usar operadores lógicos (como and/or) en números los convierte a booleanos
para la evaluación, pero devuelven su valor original (sin conversión).
No confundas esto con bool(ints) y operaciones bit a bit (&, |).
bool(0) # => False bool(2) # => True 0 and 2 # => 0 bool(-5) # => True bool(2) # => True -5 or 0 # => -5

La igualdad se comprueba con ==
1 == 1 # => True 2 == 1 # => False

La desigualdad se comprueba con !=
1 != 1 # => False 2 != 1 # => True

Más comparaciones
1 < 10 # => True 1 > 10 # => False 2 <= 2 # => True 2 >= 2 # => True

Comprobando si un valor está en un rango
1 < 2 and 2 < 3 # => True 2 < 3 and 3 < 2 # => False

Encadenar comparaciones lo hace más claro
1 < 2 < 3 # => True 2 < 3 < 2 # => False

(is vs. ==): "is" comprueba si dos variables se refieren al mismo objeto,
mientras que "==" comprueba si los objetos tienen el mismo valor.
a = [1, 2, 3, 4] # "a" apunta a una nueva lista [1, 2, 3, 4] b = a # "b" apunta a la misma lista que "a" b is a # => True,
"a" y "b" apuntan al mismo objeto b == a # => True, los objetos de "a" y "b" son iguales b = [1, 2, 3, 4] # "b" apunta a una nueva lista
[1, 2, 3, 4] b is a # => False, "a" y "b" no apuntan al mismo objeto b == a # => True, los objetos de "a" y "b" son iguales


Fuente: https://learnxinyminutes.com/docs/python/
