#include <iostream>
#include <stdlib.h>
using namespace std;

float D;

class Datos{
	
	private:
	string nombre;
	string estado;
    int edad;
    
	
	public:
	void asigna(){
            cout<<"Ingrese Nombre del Titular de la nueva cuenta : ";
            cin>>nombre;
            cout<<"Ingrese Estado de residencia: ";
            cin>>estado;
		    cout<<"Ingrese Edad: ";
		    cin>>edad;
			cout<<"\n\t\t**Datos Registrados**\n"; }
			
		string obt_nombre(){
			return nombre;
		}
};

class Cuenta:public Datos{
	
	private:
		float C;
		
	public:
		Cuenta(string, float);
		void ingresar();
		void retirar();
		void pedirsaldo();
};



Cuenta::Cuenta(string _Titular, float _C){
	obt_nombre()= _Titular;
	C= _C;
}

void Cuenta::ingresar(){
	float C1=0;
	asigna();
	C=D;
	cout<<"Saldo actual: "<<C<<endl;
	cout<<"Cantidad a depositar: "<<endl;
	cin>>C1;
	C=C+C1;
	D=C;
	cout<<"Nuevo Saldo: "<<C<<endl;
	cout<<"\n"<<endl;
}

void Cuenta::pedirsaldo(){
	cout<<"Titular: "<<obt_nombre()<<endl;
	cout<<D<<endl;
	cout<<"\n"<<endl;
}

void Cuenta::retirar(){
	float C1=0;
	
	C=D;
	
	cout<<"Titular: "<<obt_nombre()<<endl;
	cout<<"Saldo actual: "<<C<<endl;
	cout<<"Cantidad a retirar: "<<endl;
	cin>>C1;
	if(C1<(D*.96)){
		C=C-C1;
	}else{
		cout<<"La cantidad ingresada es mayor al total de su cuenta"<<endl;
	}
	
	D=C;
	cout<<"Nuevo saldo: "<<C<<endl;
	cout<<"\n"<<endl;
}

int main(){
	int O,a;
	int op;
	string T;
	
	cout<<" BIENVENIDO "<<endl;
	cout<<"Ingrese Titular de la cuenta: "<<endl;
	cin>>T;
	cout<<"Ingrese cantidad de dinero para abrir su cuenta: "<<endl;
	cin>>D;
	
	do{
		system("cls");
		cout<<"******MENU******"<<"\n"<<"1-Ingresar dinero a la cuenta"<<"\n"<<"2-Retirar efectivo"<<"\n"<<"3-Consultar Saldo"<<endl;
		Cuenta CC(T,D);
		
		cout<<"Que operacion desea realizar: "<<endl;
		cin>>O;
		switch(O){
			case 1: cout<<"Ingresar"<<endl;
			        CC.ingresar();
			break;
			
			case 2: cout<<"Retirar"<<endl;
			        CC.retirar();
			break;
			
			case 3: cout<<"Consultar Saldo"<<endl;
			        CC.pedirsaldo();
			break;
		}
	cout<<"Si desea realizar otra Operacion, por favor ingrtese otro numero diferente de 0"<<endl;
	cin>>op;
	cout<<"\n"<<endl;
}while(op != 0);

system("pause");

}
