#include <iostream>
#include <conio.h>
using namespace std;

class A{
	int a; 
	
	public:
	void Asigna_a(){
	    cout<<"Asinga valor a: "<<endl;
	    cin>>a;}
		int Obt_a(){
			return a;
		}
	};

class B{
	int b; 
	
	public:
		void Asigna_b(){
		cout<<"Asinga valor b: "<<endl;
	    cin>>b;}
		int Obt_b(){
			return b;
		}
	};

class C:public A, public B{
	int c;
	
	public:
		void mul(){
		c=Obt_a()*Obt_b();}
		Ver(){
			cout<<"valor de c: "<<c<<endl;
		}
	};
	
main(){
	
	C obd;
	
	obd.Asigna_a();
	obd.Asigna_b();
	obd.Obt_a();
	obd.Obt_b();
	obd.mul();
	obd.Ver();


getch();

}

