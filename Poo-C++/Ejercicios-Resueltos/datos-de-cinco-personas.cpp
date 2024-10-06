#include <iostream>
using namespace std;

struct hora{
	int hrs,min;
};

struct trabajador{
	int no;
	char nombre[10];
	float suel[3];
	hora entrada, salida;
};

void imprimir(trabajador a[]);

int main(){
	
    trabajador a[3];
    for (int i=0; i<3; i++){
        cout <<"Escriba el Numero de Empleado "<<i+1<<":";
        cin >> a[i].no;

        cout <<"\nEscriba el Nombre del Empleado "<<i+1<<":";
        cin >> a[i].nombre;

        cout<<"Hora de entrada(hrs)'espacio'(min): ";
		cin>>a[i].entrada.hrs>>a[i].entrada.min;
		
		cout<<"Hora de salida(hrs)'espacio'(min): ";
		cin>>a[i].salida.hrs>>a[i].salida.min;	

        cout<<"\nIngrese los tres sueldos del trabajador";
		for(int j=0; j<3; j++){
			cout<<"\nIngrese el sueldo: ";
			cin>>a[i].suel[j];
		}
        
        cout <<endl;
    }

    cout<<"\n\t\t\t\t\t'''REGISTRO DE TRABAJADORES'''  \n\n";
    imprimir(a);
    

   return 0;

}

//FUNCIONES DE USUARIO

void imprimir(trabajador a[]){
	
	cout<<"\tNumero----------Nombre--------H.Entrada-------H.Salida------------------------Sueldos--------------\n";

    for (int i=0; i<3; i++){
        cout<<"\n\t"<<a[i].no;
        cout<<"\t\t"<<a[i].nombre;
        cout<<"\t\t"<<a[i].entrada.hrs<<":"<<a[i].entrada.min;
        cout<<"\t\t"<<a[i].salida.hrs<<":"<<a[i].salida.min;
        for(int j=0; j<3; j++){
        	cout<<"\t\t"<<a[i].suel[j];
		}
   }
}


void suma(trabajador a[]){
	
}