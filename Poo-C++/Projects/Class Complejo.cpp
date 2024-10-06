#include <iostream>
using namespace std;

class Complejo{
	int a,b;
	
	public:
		void AsignaDatos(int,int);
		void Imprime();
		friend Complejo Suma (Complejo, Complejo);
};

void Complejo::AsignaDatos(int, int){
	cout<<"Ingrese a y b del numero complejo de forma 'a+bi':";
	cin>>a>>b;
}

void Complejo::Imprime(){
	int c;
	cout<<"El numero complejo es: ";
	cout<<a<<"+"<<b<<"i"<<endl;
}

Complejo Suma (Complejo x, Complejo y){
	Complejo aux;
	aux.a = x.a + y.a;
	aux.b = x.b + y.b;
	
	return aux;
}

main(){
	
	Complejo c1,c2,c3,aux;
	
	c1.AsignaDatos(1,2);
	c2.AsignaDatos(1,2);
	c3.AsignaDatos(1,2);
	c1.Imprime();
	c2.Imprime();
	c3.Imprime();
	
	aux = Suma (c1, c2);
	cout<<"\nLa suma de los numeros complejos 1 y 2"<<endl;
	aux.Imprime();
	
}


