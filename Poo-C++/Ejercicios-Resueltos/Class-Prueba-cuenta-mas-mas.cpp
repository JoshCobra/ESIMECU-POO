#include <iostream>
#include <conio.h>

using namespace std;

class Prueba{
	int codigo;
	static int cuenta;
	public:
		void AsignaCodigo(){
			codigo = cuenta++;
		}
		void MostrarCodigo(){
			cout<<"Num del Objeto: "<<codigo<<endl;
		}
		static mostrarCuenta(){
		cout<<"Cuenta: "<<cuenta<<endl;
		}
};

	int Prueba::cuenta = 10;

int main(){

	Prueba t1, t2, t3;
	
	t1.AsignaCodigo();
	t2.AsignaCodigo();
	Prueba::mostrarCuenta();	
	t3.AsignaCodigo();
	Prueba::mostrarCuenta();
	t1.MostrarCodigo();
	t2.MostrarCodigo();
	t3.MostrarCodigo();
	Prueba::mostrarCuenta();
	
	getch();
}