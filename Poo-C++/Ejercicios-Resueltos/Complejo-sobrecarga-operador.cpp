#include <iostream>
using namespace std;

class Complejo{
	int a,b;
	
	public:
		Complejo();
		Complejo(int, int);
		Complejo(int);
		
		void Ver();
		friend Complejo Suma (Complejo, Complejo);
		friend Complejo operator-(Complejo);
};

		void Complejo::Ver(){
			cout<<"\n"<<a<<"+"<<b<<"i"<<endl;
		}

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

Complejo operator-(Complejo o){
	return Complejo (-o.a,-o.b);
	
}

main(){
	
	cout<<"\n\t ---PROGRAMA NUMEROS COMPLEJOS---"<<endl;
	
	Complejo c1,c2(10,7),c3(10),cl;
	Complejo obj=Complejo(6,7);
	Complejo q=Complejo();
	
	-c1;
	-c2;
	
	
	cl = Suma (c2, c3);
	cout<<"\nLa suma de los numeros complejos 2 y 3"<<endl;
	cl.Ver();
	-cl;
	cl.Ver();
	
}