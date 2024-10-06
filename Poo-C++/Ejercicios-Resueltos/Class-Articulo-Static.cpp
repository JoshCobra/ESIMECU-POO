#include <iostream>
#include <conio.h>
#define tam 50

using namespace std;

class Articulo{
	
	private:
	int id;
	float precio;
	static int n;
	
	public:
		void AsignarDatos(int, float);
		void Ver(Articulo obj[]);
		float SumarPrecios();
		
        static Cuenta(){
		cout<<"Cuenta: "<<n<<endl;
		}
};

void Articulo::AsignarDatos(int a, float p){
	cout<<"Ingrese el id del articulo: "<<endl;
	cin>>a;
	cout<<"Ingrese el precio del producto: "<<endl;
	cin>>p;
	
	id = n++;
}	


void Articulo::Ver(Articulo obj[]){
	int cant;
cout<<"\tID----------Precio-------------------------------Precio Total (Suma)-------------------------------------------\n";

    for (int i=0; i<cant; i++){
        cout<<"\n\t"<<id;
        cout<<"\t\t"<<precio;
   }
   cout<<"\n\n\t------------------------------------------------------------------------------------------------------\n";
}

 
 int Articulo::n = 0;
 
main(){

	int a, p, cuantos;
	int y=0;
	
	cout<<"Quiere agregar un articulo? pulsa '1' ";
	cin>>y;
	
	while(y == 1){

	Articulo obj[tam];
	
	obj[tam].AsignarDatos(a, p);
	obj[tam].Ver(obj);
	
	Articulo::Cuenta();

}

getch();

}
