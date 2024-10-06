#include <iostream>
#include <stdlib.h>

using namespace std;

class Datos{

		string nombre;
		int edad;
		
	public:
		void asignar(){
	    cout<<"Ingresa Nombre de recluso: ";
	    cin>>nombre;
	    cout<<"Ingresa Edad: ";
	    cin>>edad;}
	        
		int obt_edad(){
			return edad;}
				
		string obt_nom(){
			return nombre;}	
};

class Recluso:private Datos{
	
		int no,celda;
		
	public:
		
	    void usar_asig(){
	    cout<<"Ingresa No. de Recluso: ";
	    cin>>no;
	    cout<<"Ingresa No. de Celda: ";
	    cin>>celda;
		asignar();}
		
		void buscar(){
			int srch;
			cout<<"Ingresa No. de recluo a Buscar: ";
			cin>>srch;
				if(no==srch){
					cout<<"Encontrado";
					ver();
				}else{
					cout<<"Recluso no registrado";
				}
			}
	
		void ver(){
	    cout<<no<<"\t"<<obt_nom()<<"\t\t"<<obt_edad()<<"\t\t"<<"\t\t"<<celda<<"\n";}
};

class DMedicos:public Datos{
	
		string condicion,tasn;
		int N_emp;
		
	public:
		
		void asignar_(){
	    cout<<"Ingresa condicion saludable/enfermo: ";
	    cin>>condicion;
	    cout<<"Ingresa tipo de sangre: ";
	    cin>>tasn;}

		void ver_(){
    	cout<<obt_nom()<<"\t\t"<<obt_edad()<<"\t\t"<<condicion<<"\t\t"<<tasn<<"\t\t";}
};

class Administrador:protected Datos{

		string puesto,tasn;
		
	public:
		
		void usar(){
    	asignar();
	    cout<<"Ingrese puesto: ";
    	cin>>puesto;
    	cout<<"Ingrese tasn: ";
    	cin>>tasn;}
    	
		void Ver_(){
    	cout<<obt_nom()<<"\t\t"<<obt_edad()<<"\t\t"<< puesto<<"\t\t"<< tasn<<"\n";}
};


main(){
	
	int opcion,letra,i=0,k=0,l=0;
	Recluso obj[5];
	DMedicos obj1[5];
	Administrador obj2[5];
	
	do{
	cout<<"\t\n\tMENU\n\n";
	cout<<"1) Ingresar Recluso"<<endl;
	cout<<"2) Ingresar Datos Medicos"<<endl;
	cout<<"3) Bsucar"<<endl;
	cout<<"4) Ver Reclusos"<<endl;
	cout<<"\nSelecione una opcion: ";
	cin>>opcion;
	
		switch(opcion){
			case 1:
				obj[i].usar_asig();
				i++;
				system("cls");
				break;
			case 2:
				obj1[k].asignar_();
				k++;
				system("cls");
				break;
			case 3:
				obj[i].buscar();
				i++;
				break;
			case 4:
			cout << "\nNo.Recluso-------Nombre-------Edad-------------No.Celda\n";
				for(int j=0; j<i; j++){
                    obj[j].ver();}
				break;	
		}
	cout<<"\nQuieres hacer otra cosa?\n 1)Si\n 2)No\n";
	cout<<": ";
	cin>>letra;
	}while(letra==1);
} 