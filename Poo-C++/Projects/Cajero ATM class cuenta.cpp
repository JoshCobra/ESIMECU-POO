#include <iostream>
#include <stdlib.h>
using namespace std;

float D;

class Cuenta{
	
	private:
		string Titular;
		float C;
		
	public:
		Cuenta(string, float);
		void ingresar();
		void retirar();
		void pedirsaldo();
};

Cuenta::Cuenta(string _Titular, float _C){
	Titular= _Titular;
	C= _C;
}

void Cuenta::ingresar(){
	float C1=0;
	cout<<"Titular: "<<endl;
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
	cout<<"Titular: "<<Titular<<endl;
	cout<<D<<endl;
	cout<<"\n"<<endl;
}

void Cuenta::retirar(){
	float C1=0;
	
	C=D;
	
	cout<<"Titular: "<<Titular<<endl;
	cout<<"Saldo actual: "<<C<<endl;
	cout<<"Cantidad a retirar: "<<endl;
	cin>>C1;
	if(C1<(D*.96)){
		C=C-C1;
	}else{
		cout<<"La cantidad ingresada es mayor al total de su ceunta"<<endl;
		cout<<"Se cobra un interes mensual de 4% por lo tanto la cuenta no puede estar vacia"<<endl;
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
int dia=29;
dia++;
if(dia==30){
	D=(D*.96);
	cout<<"Se he llegado al plazo de 30 dias, por lo tanto se cobrara el 4% del total de su cuenta"<<endl;
	cout<<"Su nuevo saldo es de: "<<D<<endl;
}

system("pause");

}
