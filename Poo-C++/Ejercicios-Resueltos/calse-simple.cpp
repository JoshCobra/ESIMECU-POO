#include<iostream>
#include<conio.h>
using namespace std;


class Producto{
	private:
		int id;
	public:
		float precio;

void asignar(int i, float p){

	id=i;
	precio=p;
}

void ver(){

	cout<<"id: "<<id<<endl<<"$"<<precio;
}
};


main(){

Producto obj;
obj.asignar(14,38.5);
obj.ver();
cout<<"\n"<<"ingresa el nuevo precio del producto: "<<"\t";
cin>>obj.id;
obj.ver();

}