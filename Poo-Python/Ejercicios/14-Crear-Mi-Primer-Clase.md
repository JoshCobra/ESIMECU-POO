# Ejercicio: Crear tu primera clase en Python

En este ejercicio, aprenderás a crear tu primera clase en Python. Sigue los pasos a continuación para definir una clase simple y crear instancias de ella.

## Instrucciones

1. **Definir la clase**:
    - Crea una nueva clase llamada `Persona`.
    - La clase debe tener un método especial `__init__` que inicialice los atributos `nombre` y `edad`.

2. **Agregar métodos**:
    - Añade un método llamado `saludar` que imprima un mensaje de saludo que incluya el nombre de la persona.

3. **Crear instancias**:
    - Crea dos instancias de la clase `Persona` con diferentes nombres y edades.
    - Llama al método `saludar` para cada instancia.

## Ejemplo de código

```python
class Persona:
     def __init__(self, nombre, edad):
          self.nombre = nombre
          self.edad = edad

     def saludar(self):
          print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear instancias de la clase Persona
persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 30)

# Llamar al método saludar
persona1.saludar()
persona2.saludar()
```

## Objetivos

- Comprender la sintaxis básica para definir una clase en Python.
- Aprender a inicializar atributos de una clase.
- Practicar la creación y uso de métodos dentro de una clase.
- Crear y manipular instancias de una clase.
