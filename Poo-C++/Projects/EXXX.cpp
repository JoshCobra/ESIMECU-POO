#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;

class Tiempo{
	
	friend void Calcula (Tiempo, a,b,c);
	
	private:
		
 int a,b,c;
			
	public:

 void PonTiem();

 void LeeDatos();

};

void Tiempo::PonTiem(){

cout<<"\t\tIPN/ESIME";

cout<<endl<<"\t\tI.C.E."<<endl;

}

void Timepo::LeeDatos(){

cout<<"Introduce a b c";

cin>>a>>b>>c;

}

void Calcula (Timepo, M){
int R;

R=M.a+M.b+M.c;

cout<<endl<<"Calculo de la suma ="<<R;

}

void main (){
	
	Timepo M;
	
	M.PonTiem();

    M.LeeDatos();

    Calcula(M);

   getch();

}