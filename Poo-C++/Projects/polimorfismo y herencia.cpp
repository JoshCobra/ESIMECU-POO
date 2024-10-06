#include <iostream>
#include<stdlib.h>
using namespace std;


class Automovil { //Clase Madre o Clase Principal

private://Encapsulamiento de tipo PRIVADO para los atributos de la clase madre
    string marca;
    int numpasajeros;

public: //Encapsulamiento de tipo PUBLICO para los metodos de la clase madre
    Automovil(string, int);//CONSTRUCTOR con PARAMETROS de la clase madre
    virtual void modelo(); //virtual permitira el POLIMORFISMO
};

class Motocicleta : public Automovil { //Clase hija o subclase

private: //Encapsulamiento de tipo PRIVADO  para los atributos de la calse hija
    int precio;

public: //Encapsulamiento de tipo PUBLICO para los metodos de la clase hija
    Motocicleta(string, int, int); //CONSTRUCTOR con PARAMETROS de la clase hija
    void modelo();
};

class Trailer: public Automovil{ //clase hija o subclase

private: //Encapsulamiento de tipo PRIVADO  para los atributos de la calse hija
    int numremolques;

public: //Encapsulamiento de tipo PUBLICO para los metodos de la clase hija
    Trailer(string, int, int); //CONSTRUCTOR con PARAMETROS de la clase hija
    void modelo();
};

//CONSTRUCTOR de la clase madre
Automovil::Automovil(string _marca, int _numpasajeros){
    marca = _marca;
    numpasajeros = _numpasajeros;
}

//CONSTRUCTOR de la clase hija MOTOCICLETA
Motocicleta::Motocicleta(string _marca, int _numpasajeros,int _precio) : Automovil(_marca,_numpasajeros){
    precio = _precio;
}

//CONSTRUCTOR de laclase hija TRAILER
Trailer::Trailer(string _marca, int _numpasajeros,int _numremolques) : Automovil(_marca,_numpasajeros) {
    numremolques = _numremolques;
}

//CREACION DE METODOS para cada CLASE
void Automovil::modelo() {
    cout << "La marca del vehiculo es: " << marca << endl;
    cout << " Puede tranportar: " << numpasajeros << " pasajeros" << endl;
}
void Motocicleta::modelo() {
    Automovil::modelo(); //POLIMORFISMO
    cout << "El precio de esta motocicleta es de: " << precio << " pesos" << endl;
}
void Trailer::modelo() {
    Automovil::modelo(); //POLIMORFISMO
    cout << "Este trailer puede transportar hasta: " << numremolques << " remolques" << endl;
}


//Programa Principal
int main(){
    //ARREGLO CON PUNTEROS 
    Automovil* vector[3];
    vector[0] = new Motocicleta("Yamaha",2,18000);
    vector[1] = new Trailer("volvo", 3, 1);
    vector[2] = new Automovil("Nissan", 4);
    
    vector[0]->modelo();
    vector[1]->modelo();
    vector[2]->modelo();

    system("pause");
    return 0;
}