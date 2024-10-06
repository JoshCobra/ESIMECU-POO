#include <iostream>
#include <conio.h>
using namespace std;

class Tiempo;

class Tiempo{
	private:
		int hrs,min;
		
	public:
		float a;

void asignar(){
	cout<<"ingrese hrs 'espacio' min";
	cin>>obj.hrs<<obj.min;
}

void ver(){

	cout<<"hora: "<<hrs<<":"<<min<<endl;
}
};


main(){

Tiempo obj;
obj.asignar();
obj.ver();

}