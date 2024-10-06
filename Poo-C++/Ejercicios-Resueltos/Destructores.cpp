#include <iostream>

using namespace std;

class A{

	int x;
	static int cuenta;
	
	public:
		A();
		A(int);
		
		void ver();
	
	~A(); //DESTRUCTOR
};

A::A(){
	x=0;
	cuenta++;
	cout<<"Objeto Creado"<<cuenta<<endl;}

A::A(int h){
	x=h;
	cuenta++;
	cout<<"Objeto Creado"<<cuenta<<endl;}
	
void A::ver(){
	cout<<x<<endl;}

A::~A(){
	cout<<"Objeto Destruido"<<cuenta--<<endl;}
	
int A::cuenta;		

int main(){

	A o1(2), o3;
	
	o1.ver();
	o3.ver();
	{A o2;
	o2.ver();}
	{A o4;
	o4.ver();
	}

return 0;

}
