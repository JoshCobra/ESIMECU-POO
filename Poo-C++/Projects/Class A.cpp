#include <iostream>
#include <conio.h>

using namespace std;

class A{
	
	private:
	int v1;
	int v2;
	
	public:
		void Asigna(int, int);
		void Ver();
		friend int Suma(int, int);
};


void A::Asigna(int a, int b){
	v1 = a;
	v2 = b;
}	

void A::Ver(){
	cout<<"\n\tvalor v1: "<<v1<<" valor v2: "<<v2;
}

int Suma (int a, int b){
	return a + b;
}
 
 
main(){
	
	int a, b;
	
	A obj;
	
	obj.Asigna(1, 1);
	obj.Ver();
	cout<<"\n\tsuma de a + b es: "<<Suma(a, b);

getch();

}
