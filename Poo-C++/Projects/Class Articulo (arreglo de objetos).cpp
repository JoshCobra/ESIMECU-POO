#include <iostream>
#include <conio.h>
#define tam 50

using namespace std;

class Articulo{
	
	private:
	int id[tam];
	int n;
	float precio[tam];
	
	public:
		void AsignarDatos(int, float);
		void Ver();
		float SumarPrecios();
};

void Articulo::AsignarDatos(int a, float p){
	cout<<"Ingrese el id del articulo: "<<endl;
	cin>>a;
	cout<<"Ingrese el precio del producto: "<<endl;
	cin>>p;
}	


void Articulo::Ver(){
	
	cout<<"\n\t"<<id;
    cout<<"\t\t"<<precio;

}

 
 
main(){

	int a, p, cuantos;
	
	cout<<"Cuantos articulos quiere ingresar: "<<endl;
	cin>>cuantos;
	
	Articulo obj;
	
	obj.AsignarDatos(a, p);
	obj.Ver();

getch();

}
