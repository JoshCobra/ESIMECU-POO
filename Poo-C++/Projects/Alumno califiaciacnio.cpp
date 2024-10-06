#include <iostream>

using namespace std;

class Alumno{
	
	string nombre;
		int bol;
		
	public:
		void asignar(){
	    cout<<"Ingresa nombre: ";
	    cin>>nombre;
	    cout<<"Ingresa boleta: ";
	    cin>>bol;}
	        
		int obt_bol(){
			return bol;}
				
		string obt_nom(){
			return nombre;}	
};

class Optativa:private Final{
	
	int c1;
	
	public:
		void cal_opt(){
			cout<<"Calificacion optativa: "
			cin>>c1;}
		float obt_opt(){
			return c1;}
};

class Parcial:public Alumno{

		float c1, c2;
		
	public:
		void asignar(){
	    cout<<"Ingresa Calificacion 1: ";
	    cin>>c1;
	    cout<<"Ingresa Calificacion 2: ";
	    cin>>c2;}
	        
		float obt_ca1(){
			return c1;}
				
		float obt_ca2(){
			return c2;}	
};

class Final:public Parcial{
	
		float prom; 
		
	public:
		
	    void promedio(){
	    cout<< c1+c2/2;}
	
		void ver(){
	    cout<<obt_nom()<<"\t\t"<<obt_bol()<<"\t\t"<<obt_ca1<<"\t\t"<<obt_ca2<<"\n";}
};

main(){
	
	int opcion,letra,i=0,k=0,l=0;
	Alumno obj[5];
	Optativa obj2[5];
	Final obj3[5];
	
	do{
	cout<<"\t\n\tMENU\n\n";
	cout<<"1) Ingresar Alumno"<<endl;
	cout<<"4) Ver Alumnos"<<endl;
	cout<<"\nSelecione una opcion: ";
	cin>>opcion;
		switch(opcion){
			case 1:
				obj[i].usar_asig();
				i++;
				system("cls");
				break;
			case 2:
				obj1[k].asignar_();
				k++;
				system("cls");
				break;
			case 3:
				obj2[l].usar();
				l++;
				system("cls");
				break;
			case 4:
			cout << "\nNombre-------Calificacion--------------Boleta---------------Semestre\n";
				for(int j=0; j<i; j++){
                    obj[j].ver();}
				break;
	
		}
	cout<<"\nQuieres hacer otra cosa?\n 1)Si\n 2)No\n";
	cout<<": ";
	cin>>letra;
	}while(letra==1);
} 