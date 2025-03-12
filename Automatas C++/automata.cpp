#include <iostream>
#include <cctype>
#include <string>

using namespace std;

// Estados del autómata
enum Estado {
    INICIO,
    IDENTIFICADOR,
    NUMERO,
    ASIGNACION,
    CORCHETE_ABIERTO,
    CORCHETE_CERRADO,
    COMA, 
    PUNTO_Y_COMA,
    ERROR
};

// Función para verificar si es una letra o un guion bajo (válido en identificadores)
bool esLetra(char c) {
    return isalpha(c) || c == '_';
}

// Función para verificar si es un número
bool esDigito(char c) {
    return isdigit(c);
}

// Función para el autómata finito
bool automata(string cadena) {
    Estado estado = INICIO;

    for (size_t i = 0; i < cadena.length(); i++) {
        char c = cadena[i];

        switch (estado) {
            case INICIO:
                if (esLetra(c)) estado = IDENTIFICADOR;
                else if (esDigito(c)) estado = NUMERO;
                else if (c == '=') estado = ASIGNACION;
                else if (c == '[') estado = CORCHETE_ABIERTO;
                else if (c == ',') estado = COMA;
                else if (c == ';') estado = PUNTO_Y_COMA;
                else return false; // Caracter inválido
                break;

            case IDENTIFICADOR:
                if (esLetra(c) || esDigito(c)) estado = IDENTIFICADOR;
                else if (c == '=') estado = ASIGNACION;
                else if (c == '[') estado = CORCHETE_ABIERTO;
                else if (c == ',') estado = COMA;
                else if (c == ';') estado = PUNTO_Y_COMA;
                else return false;
                break;

            case NUMERO:
                if (esDigito(c)) estado = NUMERO;
                else if (c == ',') estado = COMA;
                else if (c == ';') estado = PUNTO_Y_COMA;
                else return false;
                break;

            case ASIGNACION:
                if (esDigito(c) || esLetra(c)) estado = IDENTIFICADOR;
                else return false;
                break;

            case CORCHETE_ABIERTO:
                if (esDigito(c) || esLetra(c)) estado = IDENTIFICADOR;
                else return false;
                break;

            case CORCHETE_CERRADO:
                if (c == ',') estado = COMA;
                else if (c == ';') estado = PUNTO_Y_COMA;
                else return false;
                break;

            case COMA:
                if (esLetra(c)) estado = IDENTIFICADOR;
                else return false;
                break;

            case PUNTO_Y_COMA:
                return (i == cadena.length() - 1); // Solo debe estar al final

            case ERROR:
                return false;
        }
    }

    return estado == PUNTO_Y_COMA; // La cadena es válida si termina en `;`
}

int main() {
    string prueba2 = "12;";
    string prueba = "l=7, j, A[5][m][r], p=k, q, n, B[a], r=C[3][z];";

    if (automata(prueba)) {
        cout << "Cadena válida." << endl;
    } else {
        cout << "Cadena inválida." << endl;
    }

    if (automata(prueba2)) {
        cout << "Cadena válida." << endl;
    } else {
        cout << "Cadena inválida." << endl;
    }

    return 0;
}
