
//SISTEMA DE MAXIMA SEGURIDAD

#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;

class fecha{
	public:
		
	int dia, mes, ano;
	int hrs,min;
};

class recluso{
	public:
		
	int no;
	char nombre[10];
	char apellido_P[10];
	char apellido_M[10];
	int sent_a;
	int sent_m;
	fecha entrada;
};

void imprimir(recluso a[], int cant);

main(){

	recluso a[10];
	int cant;
	cout<<"\n\nNumero de reclusos que va a ingresar: ";
	cin>>cant;
	

    for (int i=0; i<cant; i++){

    	cout<<"\n\nINGRESE LOS DATOS DEL RECLUSO";
    	        cout<<"\n\nEscriba el Numero de Recluso "<<i+1<<": ";
        cin>>a[i].no;

        cout<<"\nEscriba el Nombre del Recluso "<<a[i].no;
        cout<<"\nNombre  'espacio'  Apellido Paterno  'espacio'  Apellido Materno"<<endl;
        cin>>a[i].nombre>>a[i].apellido_P>>a[i].apellido_M;
        
        cout<<"\n\nINGRESE FECHA DE INGRESO DEL RECLUSO";
        
        cout<<"\nEscriba Dia(00)  'espacio'  Mes(00)  'espacio'  Anio(0000): ";
        cin>>a[i].entrada.dia>>a[i].entrada.mes>>a[i].entrada.ano;

        cout<<"\nEscriba Hora de entrada(hrs)'espacio'(min): ";
		cin>>a[i].entrada.hrs>>a[i].entrada.min;

        cout<<"\nIngrese la sentencia del recluso en Anios 'espacio' meses: ";
		cin>>a[i].sent_a>>a[i].sent_m;
        cout<<endl;
        }

    imprimir(a,cant);
    
   return 0;

}

//FUNCIONES DE USUARIO

void imprimir(recluso a[], int cant){
	
	cout<<"\tNumero--------------Nombre---------------------Entrada-Fecha----Hora----------------Sentencia-------------\n";

    for (int i=0; i<cant; i++){
        cout<<"\n\t"<<a[i].no;
        cout<<"\t\t"<<a[i].nombre<<" "<<a[i].apellido_P<<" "<<a[i].apellido_M;
        cout<<"\t\t"<<a[i].entrada.dia<<"/"<<a[i].entrada.mes<<"/"<<a[i].entrada.ano;
        cout<<"\t"<<a[i].entrada.hrs<<":"<<a[i].entrada.min;
        cout<<"\t\t"<<a[i].sent_a<<" Anios "<<a[i].sent_m<<" Meses ";

   }
   cout<<"\n\n\t----------------------------------------------------------------------------------------------------------\n";
}