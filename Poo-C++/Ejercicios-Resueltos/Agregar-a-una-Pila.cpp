
#include<iostream>
#include<conio.h>
using namespace std;


struct Nodo{
	int dato;
	Nodo *sig;
	
};

void agregarPila(Nodo *&,int);
void mostrarPila(Nodo *&,int&);

int main()
{
	Nodo *pila = NULL;
	int dato;
	char rpt;
	
	do{
		cout<<"ingresa un numero: ";
		cin>>dato;
		agregarPila(pila,dato);
		
		cout<<"\nDesea agregar otro elemento a la pila (s/n): ";
		cin>>rpt;
	}while(rpt=='s');
	
	cout<<"\n Mostrando elelmentos de pila: ";
	while(pila != NULL){
		mostrarPila(pila,dato);
		if(pila != NULL){
			cout<<dato<<",";
		}
		else{
			cout<<dato<<".";
		}
	}
	
	getch();
	return 0;
}

void agregarPila(Nodo *&pila,int n){
	Nodo *nuevo_nodo = new Nodo();
	nuevo_nodo->dato = n;
	nuevo_nodo->sig = pila;
	pila = nuevo_nodo;
	
	cout<<"\tElemento "<<n<<" ha sido agregado correctamente ";
}


void mostrarPila(Nodo *&pila,int &n){
	Nodo *aux = pila;
	n = aux->dato;
	pila = aux->sig;
	delete aux;
}