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
cout<<"\n\n\tID-------------Precio-----------------Precio Total (Suma)------------------------------------------\n";

    for (int i=0; i<cant; i++){
        cout<<"\n\t"<<id;
        cout<<"\t     "<<precio;
   }
   cout<<"\n\n\t---------------------------------------------------------------------------------------------------\n\n\n";
}

 
 int Articulo::n = 0;
 
main(){

	int a, p, cuantos;
	int y=0;
	
	Articulo obj[tam];
	
	int x=0;
	cout<<"Presiona '4' para ver el menu  ";
    cin>>x;
    
	while(x>3){
	
	cout<<"------------------------------M E N U------------------------------------"<<endl;
	cout<<"\t\tSELECCIONE LA OPCION QUE QUIERE REALIZAR"<<endl;
	cout<<"\nIngresa '1' para AGREGAR UN ARTICULO"<<endl;
	cout<<"\nIngresa '2' para VER los articulos"<<endl;
	cout<<"\nIngresa '3' para SUMAR precio de los articulos"<<endl;
	cout<<"\n\t :";
	cin>>y;
	
	switch (y){
		    
    case 1: obj[tam].AsignarDatos(a, p);
    break;
            
    case 2: obj[tam].Ver(obj);
    break;
            
    case 3: Articulo::Cuenta();
    break;
    
    case 4: cout<<"";
	break;
    
    default: cout<<"SALIENDO DEL MENU"<<endl;
    
 x=0;
 
}
}

getch();

}
