#include <iostream>
#include <conio.h>

using namespace std;

class B;
class A{
	int v1;
	
	public:
		void Asigna(int);
		void Ver();
		friend int Suma(A, B);
};

void A::Asigna(int a){
	v1 = a;
}	

void A::Ver(){
	cout<<"\n\ta: "<<v1;
}


class B{
		int v2;
		
	public:
		void Asigna(int);
		void Ver();
		friend int Suma(A, B);
};

void B::Asigna(int b){
	v2 = b;
}	

void B::Ver(){
	cout<<"\n\tb: "<<v2;
}

int Suma (A a, B b){
	return a.v1 + b.v2;
}

main(){
	
	int a, b;
	
	A obj;
	B obt;
	
	obj.Asigna(1);
	obj.Ver();
	
	obt.Asigna(2);
	obt.Ver();
	
	cout<<"\n\tsuma de a + b es: "<<Suma(obj, obt);

getch();

}
