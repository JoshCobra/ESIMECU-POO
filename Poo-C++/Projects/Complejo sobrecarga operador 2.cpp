#include <iostream>
using namespace std;

class Complejo{
	int a,b;
	
	public:
		Complejo(int x, int y){
			a=x;    b=y;}
			
		Complejo(){
		a=0;	b=0;}
		
		Complejo(int x){
		a=0;    b=x;}
		
		friend Complejo Suma (Complejo, Complejo);
		friend Complejo operator+(Complejo,Complejo);
		friend Complejo operator-(Complejo,Complejo);
		friend Complejo operator-(Complejo);
		void Ver();
};

void Complejo::Ver(){
	cout<<a<<"+"<<b<<"i"<<endl;
}

Complejo operator-(Complejo o){
	return Complejo (-o.a,-o.b);
	
}

Complejo operator+(Complejo a, Complejo b){
	Complejo aua;
	aua.a=a.a+b.a;
	aua.b=a.b+b.b;
	return aua;
}

Complejo operator-(Complejo a, Complejo b){
	return Complejo (a.a-b.a,a.b-b.b);
}

Complejo Suma (Complejo x, Complejo y){
	Complejo cl;
	cl.a = x.a + y.a;
	cl.b = x.b + y.b;
	
	return cl;
}

int main(){
	
	cout<<"\n\t ---SOBRECARGA NUMEROS COMPLEJOS---"<<endl;
	
	Complejo c1,c2(10,7),c3(10),cl;
	
	-c2;
	c2.Ver();
	cl=c2+c3;
	cl.Ver();
	cl=c2-c3;
	cl.Ver();
	cl=-c3;
	cl.Ver();
	
	cl = Suma (c2, c3);
	cout<<"\nLa suma de los numeros complejos 2 y 3"<<endl;
	cl.Ver();

	return 0;
	
}