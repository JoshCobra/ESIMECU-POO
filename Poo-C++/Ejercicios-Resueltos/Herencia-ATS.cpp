#include <iostream>
#include <stdlib.h>
using namespace std;

class Persona{
	private:
		string nombre;
		int edad;
	public:
		Persona(string, int);
		void mostrarP();
};

Persona::Persona(string _nombre, int _edad){
	nombre = _nombre;
	edad = _edad;
}

void Persona::mostrarP(){
	cout << "Nombre de la persona es: " << nombre <<endl;
	cout << "Edad de la persona es: " << edad <<endl;
}

class Empleado : public Persona{
	private:
		float sueldo;
	public:
		Empleado(string, int, float);
		void mostrarE(){
			mostrarP();
			cout << "Sueldo del empleado es: " << sueldo <<endl;
		}
};

Empleado::Empleado(string _nombre, int _edad, float _sueldo) : Persona(string _nombre, int _edad){
	sueldo = _sueldo;
}

class Estudiante : public Persona{
	private:
		float notaF;
	public:
		Estudiante(string, int, float);
		void mostrarEstu();
};

Estudiante::Estudiante(string _nombre, int _edad, float _notaF) : Persona(string _nombre, int _edad){
	notaF = _notaF;
}

void Estudiante::mostrarEstu(){
	mostrarP();
	cout << "Nota final del estudiante: " << notaF <<endl;
}

class Universitario : public Estudiante{
	private:
		string instituto;
	public:
		Universitario(string, int, float, string);
		void mostrarU();
};

Universitario::Universitario(string _nombre, int _edad, float _notaF, string _instituto) : Estudiante(string _nombre, int _edad, float _notaF){
	instituto = _instituto;
}

void Universitario::mostrarU(){
	mostrarEstu();
	cout << "Instituto al que pertenece: " << instituto <<endl;
}



int main(){
	
	Empleado e1 ("ricardo", 35, 1300);
	cout << "Empleado "<<endl;
	e1.mostrarE();
	cout << endl;
	
	
	
	system ("pause");
	return 0;
}
