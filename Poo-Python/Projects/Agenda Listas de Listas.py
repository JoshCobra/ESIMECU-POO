def crear_agenda():
    agenda = {}
    return agenda

def agregar_evento(agenda):
    año = int(input("Introduce el año: "))
    mes = str(input("Introduce el mes: "))
    dia = int(input("Introduce el día: "))
    hora = str(input("Introduce la hora: "))
    evento = input("Introduce la información que deseas guardar en este evento: ")

    if año not in agenda:
        agenda[año] = {}  

    if mes not in agenda[año]:
        agenda[año][mes] = {} 

    if dia not in agenda[año][mes]:
        agenda[año][mes][dia] = {}

    agenda[año][mes][dia][hora] = evento
    print("Evento agregado")

def mostrar_eventos(agenda):
    if not agenda:  # Verifica si la agenda está vacía
        print("No hay eventos registrados en la agenda.")
        return

    print("Eventos registrados en la agenda:")
    for año, meses in agenda.items():
        for mes, dias in meses.items():
            for dia, horas in dias.items():
                for hora, evento in horas.items():
                    print("Fecha:" ,dia,"/",mes,"/",año, "- Hora:" ,hora," - Evento:" ,evento)
            #El método items() se utiliza para en este caso (agenda) tiene las horas del día 
            # como claves y los eventos como valores, este método devuelve un conjunto
            # de estos dos, es decir (hora,evento), usando el ciclo for recorremos ese conjunto
            # obteniendo la hora y la descripción del evento
            #https://docs.python.org/3/tutorial/datastructures.html

def menu():
    agenda = crear_agenda()

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar un evento")
        print("2. Mostrar eventos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_evento(agenda)
        elif opcion == "2":
            mostrar_eventos(agenda)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
