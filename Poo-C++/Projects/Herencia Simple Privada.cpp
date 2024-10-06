#include <iostream>
#include <conio.h>
using namespace std;

class B{
	int a;
	
	public:
		int b;
		void Asigna(){
				cout<<"Asinga valor a"<<endl;
	            cin>>a;}
		int Obt_a(){
			return a;}
		void Ver_a(){
			cout<<"el valor de a es: "<<a<<endl;}
};

class D:B{
		int c;
		
	public:
		void mul(){
			Asigna();
			cout<<"ingresa b: ";cin>>b;
			c=Obt_a()*b;}
		void Ver(){
			Ver_a();
			cout<<"b= "<<b;
			cout<<"c= "<<c;}
};

main(){
	
	D obd;

	obd.mul();
	obd.Ver();


getch();

}
