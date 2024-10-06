#include<iostream>
#include<conio.h>
using namespace std;


class Producto{
	private:
		int id;
		float precio;
	public:
		void asignar(int, float);
		void ver();
};

void Producto::asignar(int i, float p){
	id=i;
	precio=p;
}

void Producto::ver(){
	cout<<"\nID: "<<id<<"\t Precio: "<<"$"<<precio;
}

main(){

Producto obj;
obj.asignar(14,38.5);
obj.ver();
obj.asignar(293,23.74);
obj.ver();

//cout<<obj.id; private

}