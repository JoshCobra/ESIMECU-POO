#include <iostream>
#include <stdlib.h>
using namespace std;

class Rectangulo{
	private:
		float largo;
		float ancho;
	public:
		Rectangulo(float, float);
		void perimetro();
		void area();
};

Rectangulo::Rectangulo(float _largo, float _ancho){
	largo = _largo;
	ancho = _ancho;
}

void Rectangulo::perimetro(){
	float per;
	per = largo+largo+ancho+ancho;
	cout << "El perimetro es: " << per << " cm" <<endl;
}

void Rectangulo::area(){
	float area;
	area = largo * ancho;
	cout << "El area es: " << area << " cm2" <<endl;
}

int main(){
	Rectangulo r1(2, 6.2);
	Rectangulo r2(5.8, 9);
	Rectangulo r3(3, 7);
	Rectangulo r4(45, 59.7);
	
	cout << "Rectangulo 1: " <<endl;
	r1.area();
	r1.perimetro();
	cout <<"\n";
	
	cout << "Rectangulo 2: " <<endl;
	r2.area();
	r2.perimetro();
	cout << "\n";
	
	cout << "Rectangulo 3: " <<endl;
	r3.area();
	r3.perimetro();
	cout << "\n";
	
	cout << "Rectangulo 4: " <<endl;
	r4.area();
	r4.perimetro();
	cout << "\n";
	
	
	system("pause");
	return 0;
}