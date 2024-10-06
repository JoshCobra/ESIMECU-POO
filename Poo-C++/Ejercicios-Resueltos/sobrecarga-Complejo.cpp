#include <iostream>
using namespace std;

class Complejo{
	int a,b;
	
	public:
		Complejo();
		Complejo(int, int);
		Complejo(int);
		
		void mostrar(){
			cout<<"\n"<<a<<"+"<<b<<"i"<<endl;
		}
		
		friend Complejo Suma (Complejo, Complejo);
};

		Complejo::Complejo(int x, int y){
		    a=x;b=y;}
		
		Complejo::Complejo(){
			b=0;a=0;}
			
		Complejo::Complejo(int x){
			a=0;b=x;}

Complejo Suma (Complejo x, Complejo y){
	Complejo cl;
	cl.a = x.a + y.a;
	cl.b = x.b + y.b;
	
	return cl;
}

main(){
	
	cout<<"\n\t ---PROGRAMA NUMEROS COMPLEJOS---"<<endl;
	
	Complejo c1,c2(10,7),c3(10),cl;
	Complejo obj=Complejo(6,7);
	Complejo q=Complejo();
	
	c1.mostrar();
	c2.mostrar();
	c3.mostrar();
	q.mostrar();
	obj.mostrar();
	
	cl = Suma (c2, c3);
	cout<<"\nLa suma de los numeros complejos 2 y 3"<<endl;
	cl.mostrar();
	
}