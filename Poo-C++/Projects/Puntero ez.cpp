#include<iostream>
#include<conio.h>
#include<stdlib.h>
using namespace std;

int main(){
	
	int n;
	cout<<"cuantos numeros a ingesar: "; cin>> n;
	
	int numeros[n], *dir_numeros;
	
	for(int i=0;i<n;i++){
		cout<<"Digite un numero ["<<i<<"]: ";
		cin>>numeros[i];
	}
	
	dir_numeros = numeros; 
	
	for(int i=0;i<n;i++){
		if(*dir_numeros%2==0){
			cout<<"es par: "<<*dir_numeros<<"\tposicion: "<<dir_numeros<<endl;
		}
		dir_numeros++;
	}
	
	
	getch();
	return 0;
}
