#include <iostream>
#include <conio.h>
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

void imprimir(trabajador a[], int cant);
void suma(trabajador a[], float suel[]);

int main(){
	
		cout<<"\n\t'''INGRESE DATOS PARA EMPLEADOS'''";
	trabajador a[10];
	int cant;
	
	cout<<"\n\nNumero de trabajadores quiere ingresar: ";
	cin>>cant;
	
    for (int i=0; i<cant; i++){
    	cout<<"\n\nINGRESE LOS DATOS DEL EMPLEADO";
    	
        cout<<"\n\nEscriba el Numero de Empleado "<<i+1<<":";
        cin>>a[i].no;

        cout<<"\nEscriba el Nombre del Empleado "<<i+1<<":";
        cin>>a[i].nombre;

        cout<<"\nEscriba Hora de entrada(hrs)'espacio'(min): ";
		cin>>a[i].entrada.hrs>>a[i].entrada.min;
		
		cout<<"\nEscriba Hora de salida(hrs)'espacio'(min): ";
		cin>>a[i].salida.hrs>>a[i].salida.min;	

        cout<<"\nIngrese los tres sueldos del trabajador";
		for(int j=0; j<3; j++){
			cout<<"\nIngrese el sueldo: ";
			cin>>a[i].suel[j];
		}
        
        cout<<endl;
    }

    cout<<"\n\t\t\t\t\t  '''REGISTRO DE TRABAJADORES'''  \n\n";
    imprimir(a, cant);
    cout<<"\n\t";
    suma(a, suel);
    
   return 0;

}

//FUNCIONES DE USUARIO

void imprimir(trabajador a[], int cant){
	
	cout<<"\tNumero----------Nombre--------H.Entrada-------H.Salida-------------------------Sueldos----------------\n";

    for (int i=0; i<cant; i++){
        cout<<"\n\t"<<a[i].no;
        cout<<"\t\t"<<a[i].nombre;
        cout<<"\t\t"<<a[i].entrada.hrs<<":"<<a[i].entrada.min;
        cout<<"\t\t"<<a[i].salida.hrs<<":"<<a[i].salida.min;
        for(int j=0; j<3; j++){
        	cout<<"\t\t$"<<a[i].suel[j];
		}
   }
   cout<<"\n\n\t------------------------------------------------------------------------------------------------------\n";
}


void suma(trabajador a[], float suel[]){
		float suma = 0;
	 	float numeroActual = a->suel[];
	 	suma += numeroActual;
	 	cout<<"\n\n\t\t"<<suma;
		
	
}
