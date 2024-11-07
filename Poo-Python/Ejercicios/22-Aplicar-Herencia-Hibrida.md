# Aplicar Herencia Híbrida a los Ejercicios de la Clase 15

Implementar la herencia híbrida en los ejercicios de la clase 15.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'{self.nombre} de {self.edad} años' 
```

```python
class Escuela:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f'{self.nombre} en {self.direccion}'
```
