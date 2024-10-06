#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;

class recluso{
	
    int no;
    string nombre;
		
	public:
		void num(){
		cout<<"\n\nEscriba el Numero de Recluso "<<": ";
        cin>>no;}
        
		void asignaD(){
        cout<<"\nEscriba el Nombre del Recluso "<<no<<": ";
        cin>>nombre;}

};


class fecha{
	
	int dia, mes, anio;
	int hrs,min;
	
	public:
		int asignaF(){
			
		cout<<"\n\nINGRESE FECHA DE INGRESO DEL RECLUSO";
        
        cout<<"\nEscriba Dia(00)  'espacio'  Mes(00)  'espacio'  Anio(0000): ";
        cin>>dia>>mes>>anio;
        cout<<"\nEscriba Hora de entrada(hrs)'espacio'(min): ";
		cin>>hrs>>min;
		
		return dia, mes, anio, hrs, min;}
		
};

class C:public recluso, public fecha{
	int s;
	
	public:
		void imprimir(){
		cout<<"\tNumero--------------Nombre---------------------Entrada-Fecha----Hora----------------Sentencia-------------\n";
        cout<<"\n\n\t----------------------------------------------------------------------------------------------------------\n";
		}
	};
	
class DatosM:public recluso{
	
	char sangre;
	string enfe;
	
	public:
		void Dmedicos(){
			cout<<"INGRESA DATOS MEDICOS"<<endl;
			cout<<"Ingresa tipo de sangre: ";
			cin>>sangre;
			cout<<"Ingresa si padece alguna enfermedad: ";
			cin>>enfe;
		}
};

int menu(int tam, string arr[]){
	
	C a;
	
    int op;
    cout<<"Eliga la accion que quiera realizar:"<<endl<<"1.- Ingresar Datos"<<endl<<"2.- Ingresar Fecha"<<endl<<"3.- Ver Datos"<<endl<<"4.- Borrar"<<endl<<"5.- Salir"<<endl;
    cout<<"Introduzca una opcion: ";
    
    switch(op){
        case 1 :
            a.num();
            a.asignaD();
            break;
        case 2 :
            a.asignaF();
            break;
        case 3 :
            a.imprimir();
            break;
        case 4 :
            break;
        case 5 :
            cout<<"\t\n\tSALIENDO\n\n";
            return 0;
        break;
        default:
            cout<<"\t\n\tError de opcion\n\n";
        break;
    }
}

int main(){
	
    const int tam=15;
    int op;
    string arr[tam];

    menu(tam,arr);
    
}
