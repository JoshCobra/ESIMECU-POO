#include <iostream>

using namespace std;

class Punto {
	int x, y;
	public:
		void Asignar(int, int);
		void Ver();
		friend Punto Suma (Punto, Punto);
		friend float Pendiente (Punto, Punto);
};

void Punto::Asignar(int, int){
	int x,y;
}

void Punto::Ver(){
	
}

Punto Suma (Punto a, Punto b){
	Punto aux;
	aux.x = a.x + b.x;
	aux.y = a.y + b.y;
	
	return aux;
}

float Pendiente (Punto c, Punto d){
	float m;
	m=(d.y - c.y)/(d.x - c.x);
	
	return m;
}


int main(){
	int a, b;
	
	Punto y, pi, aux;
	
	y.Asignar(1, 2);
	pi.Asignar(10,5);
	y.Ver();
	pi.Ver();
	
	aux = Suma (y, pi);
	aux.Ver();
	cout<<Pendiente (y, pi);
	
	return 0;		
}