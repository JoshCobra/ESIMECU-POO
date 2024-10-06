#include <iostream>
#include <conio.h>
using namespace std;

class B{
	int a;
	
	public:
		int b;
		void Asigna(){
				cout<<"Asinga valor a: "<<endl;
	            cin>>a;}
		int Obt_a(){
			return a;}
		void Ver_a(){
			cout<<"el valor de a es: "<<a<<endl;}
};

class D:public B{
		int c;
		
	public:
		void mul(){
			c=Obt_a()*b;}
		void Ver(){
			cout<<"  c= "<<c<<endl;}
};

main(){
	
	D obd;
	
	obd.Asigna();
	cout<<"Ingresa b: "<<endl;
	cin>>obd.b;
	obd.mul();
	obd.Ver_a();
	cout<<"b= "<<obd.b;
	obd.Ver();


getch();

}
