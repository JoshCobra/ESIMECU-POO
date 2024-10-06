#include<iostream>
#include<conio.h>
using namespace std;


class Producto{
	private:
		int id;
		float precio;
	public:
		Producto(int,float);
		void ver();
};

Producto::Producto(int _id, float _precio){
	id = _id;
	precio = _precio;
}

void Producto::ver(){
	cout<<"\nID: "<<id<<"\t Precio: "<<"$"<<precio;
}

main(){

Producto p1 = Producto(29,92.30);
p1.ver();

Producto p2 = Producto(21,546.43);
p2.ver();

//cout<<obj.id; private

}