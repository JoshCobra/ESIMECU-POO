#include <iostream>
#include <stdlib.h>
using namespace std;

class Persona{
	private:
		int edad;
		string nombre;
		float talla;
		float peso;
	public:
		Persona(int, string, float, float);
		void informacion();
		void dieta();
};

Persona::Persona(int _edad, string _nombre, float _talla, float _peso){
	edad = _edad;
	nombre = _nombre;
	talla = _talla;
	peso = _peso;
}

void Persona::informacion(){
	cout << "Me llamo " << nombre <<endl; 
	cout << " Tengo " << edad << " anios " <<endl;
	cout << " mido " << talla << "cm" <<endl;
	cout << " y mi peso es " << peso << "kg" <<endl;
}

void Persona::dieta(){
	cout << "Mi dieta consiste de alimentos que me ayudan a mantener mi peso actual " << peso << "kg" <<endl;
	cout << "Ademas de ayudar a mi sistema inmunologico" << endl;
}

int main(){
	Persona p1(18, "Juan", 1.86, 89);
	Persona p2(23, "Sarah", 1.54, 49);
	
	p1.informacion();
	p1.dieta();
	
	p2.informacion();
	p2.dieta();
	
	system("pause");
	return 0;
	
}