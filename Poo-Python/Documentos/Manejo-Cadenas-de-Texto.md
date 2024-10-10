# Introducción al Manejo de Cadenas de Texto en Python

### Las cadenas de texto se crean usando `"` o `'`
```
"This is a string." # Esto es una cadena de texto. 'This is also a string.' # Esto también es una cadena de texto.
```
### Las cadenas también se pueden sumar (concatenar)
```
"Hello " + "world!" # => "Hello world!"
```
### Las literales de cadenas (pero no las variables) se pueden concatenar sin usar el operador '+'
```
"Hello " "world!" # => "Hello world!"
```

### Una cadena puede ser tratada como una lista de caracteres
```
"Hello world!"[0] # => 'H'
```
### Puedes encontrar la longitud de una cadena
```
len("This is a string") # => 16
```
Checa tambien en [Metodos Aplicables a Cadenas](Documentos/Metodos-Aplicables-a-Cadenas.txt) y [Ejemplo Operaciones Con Cadenas](Documentos/OperacionesConCadenas.PNG)

### Desde Python 3.6, puedes usar f-strings o cadenas de texto formateadas.
```
name = "Reiko" f"She said her name is {name}." # => "She said her name is Reiko"
```
### Cualquier expresión válida de Python dentro de las llaves se incluye en la cadena.
```
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."
```

### None es un objeto
```
None # => None
```

###  No uses el símbolo de igualdad "==" para comparar objetos con None.
Usa "is" en su lugar. Esto comprueba la igualdad de identidad de objetos.
```
"etc" is None # => False None is None # => True
```



*Fuente: https://learnxinyminutes.com/docs/python/*
