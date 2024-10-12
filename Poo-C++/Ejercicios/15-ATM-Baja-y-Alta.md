# ATM - Baja y Alta (ATM-baja-y-alta.cpp)

Objetivo: Simular un cajero automático que permite gestionar clientes y sus saldos.

### Pasos:
- ### Estructura del Cliente:

Define una clase o estructura Cliente con los atributos `nombre` y `saldo.`

### Menú de opciones:
- Alta de cliente: Agregar un cliente nuevo con nombre y saldo.
- Baja de cliente: Eliminar un cliente de la lista.
- Consultar saldo: Mostrar el saldo de un cliente.
- Depositar/Retirar dinero: Modificar el saldo del cliente.
- Salir: Finalizar el programa.
  
### Repetición:

Después de cada operación, el menú se muestra nuevamente hasta que el usuario decida salir.

### Resultado esperado:
El programa permite gestionar clientes y realizar transacciones. Ejemplo:
```
Seleccione una opción: 1
Nombre: Juan, Saldo inicial: 1000
Cliente agregado.

Seleccione una opción: 3
Nombre del cliente: Juan
Saldo: $1000

Seleccione una opción: 4
Cantidad a depositar: 500
Nuevo saldo de Juan: $1500
```
