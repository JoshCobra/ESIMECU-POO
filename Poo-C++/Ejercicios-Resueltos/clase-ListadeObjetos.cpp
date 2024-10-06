#include <iostream>
#include <string>

class A {
private:
    int serial;
    std::string nombre;
public:
    A(int _serial, const std::string& _nombre) : serial(_serial), nombre(_nombre) {}

    int getSerial() const {
        return serial;
    }

    const std::string& getNombre() const {
        return nombre;
    }
};

class ListadeObjetos {
private:
    static const int MAX_OBJETOS = 20;
    A* arreglo[MAX_OBJETOS];
    int contador;
public:
    ListadeObjetos() : contador(0) {}

    bool estaLleno() const {
        return contador >= MAX_OBJETOS;
    }

    bool estaVacio() const {
        return contador <= 0;
    }

    void agregarObjeto(A* objeto) {
        if (estaLleno()) {
            std::cout << "El arreglo esta lleno, no se puede agregar mas objetos." << std::endl;
            return;
        }
        arreglo[contador++] = objeto;
    }

    void retirarObjeto() {
        if (estaVacio()) {
            std::cout << "El arreglo esta vacio, no hay nada para retirar." << std::endl;
            return;
        }
        contador--;
        delete arreglo[contador];
        arreglo[contador] = nullptr;
    }

    void mostrarInformacion(int posicion) const {
        if (posicion < 0 || posicion >= contador) {
            std::cout << "Posicion invalida." << std::endl;
            return;
        }
        if (arreglo[posicion] == nullptr) {
            std::cout << "No hay objeto en la posicion " << posicion << "." << std::endl;
            return;
        }
        std::cout << "Informacion del objeto en la posicion " << posicion << ":" << std::endl;
        std::cout << "Serial: " << arreglo[posicion]->getSerial() << std::endl;
        std::cout << "Nombre: " << arreglo[posicion]->getNombre() << std::endl;
    }

    void mostrarInformacionTodos() const {
        if (estaVacio()) {
            std::cout << "El arreglo está vacio." << std::endl;
            return;
        }
        std::cout << "Informacion de todos los objetos:" << std::endl;
        for (int i = 0; i < contador; ++i) {
            if (arreglo[i] != nullptr) {
                std::cout << "Posicion " << i << ":" << std::endl;
                std::cout << "Serial: " << arreglo[i]->getSerial() << std::endl;
                std::cout << "Nombre: " << arreglo[i]->getNombre() << std::endl;
            }
        }
    }
};

A* nuevoObjetoLista(int serial, const std::string& nombre) {
    return new A(serial, nombre);
}

int main() {
    ListadeObjetos lista;
    int opcion;
    do {
        std::cout << "\nMenu:" << std::endl;
        std::cout << "1. Agregar objeto" << std::endl;
        std::cout << "2. Retirar objeto" << std::endl;
        std::cout << "3. Mostrar informacion de un objeto individual" << std::endl;
        std::cout << "4. Mostrar informacion de todos los objetos" << std::endl;
        std::cout << "5. Salir" << std::endl;
        std::cout << "Seleccione una opcion: ";
        std::cin >> opcion;

        switch (opcion) {
            case 1: {
                if (lista.estaLleno()) {
                    std::cout << "El arreglo esta lleno, no se puede agregar mas objetos." << std::endl;
                } else {
                    int serial;
                    std::string nombre;
                    std::cout << "Ingrese el serial del objeto: ";
                    std::cin >> serial;
                    std::cout << "Ingrese el nombre del objeto: ";
                    std::cin >> nombre;
                    A* nuevoObjeto = nuevoObjetoLista(serial, nombre);
                    lista.agregarObjeto(nuevoObjeto);
                    std::cout << "Objeto agregado correctamente." << std::endl;
                }
                break;
            }
            case 2: {
                lista.retirarObjeto();
                std::cout << "Objeto retirado correctamente." << std::endl;
                break;
            }
            case 3: {
                int posicion;
                std::cout << "Ingrese la posicion del objeto que desea mostrar: ";
                std::cin >> posicion;
                lista.mostrarInformacion(posicion);
                break;
            }
            case 4: {
                lista.mostrarInformacionTodos();
                break;
            }
            case 5: {
                std::cout << "Saliendo del programa..." << std::endl;
                break;
            }
            default: {
                std::cout << "Opción invalida. Inténtelo de nuevo." << std::endl;
                break;
            }
        }
    } while (opcion != 5);

    return 0;
}
