#include <iostream>

using namespace std;

class Datos{

		string nombre;
		int n_bol,sem;

		
	public:
	    void asignar(){
	    cout<<"Ingresa nombre: ";
	    cin>>nombre;
	    cout<<"Ingresa numero de boleta: ";
	    cin>>n_bol;
	    cout<<"Ingresa semestre: ";
	    cin>>sem;}
		
		string obt_nom(){
			return nombre;}	
		
		int obt_bol(){
	    	return n_bol;}
		
		int obt_sem(){
			return sem;}
};

class Parcial:public Datos{
	
		float c1,c2;
		
	public:
		
		void usar_asig(){

	    cout<<"Ingresa califiacion 1: ";
	    cin>>c1;
	    cout<<"Ingresa califiacion 2: ";
	    cin>>c2;}
	        
		float obt_c1(){
			return c1;}
			
		float obt_c2(){
			return c2;}
		
		void ver(){
	    cout<<obt_nom()<<"\t\t"<<obt_c1()<<"\t\t"<<obt_c2()<<"\t"<<"\t"<<obt_bol()<<"\t"<<"\t"<<obt_sem()<<"\n";}
};

class Optativa:private Final{
	
	int c1;
	
	public:
		void ingresa(){
			cout<<"ingresa cal optativa: ";
			cin>>c1;}
		int obt_opt(){
			return c1;}
};

class Final:public Parcial{
	
		int P;
		
	public:
		
		void prom(){
		P= obt_c1()+obt_c2()/2;}
		
		float promedio(){
			return P;}
};


main(){
	
	int opcion,letra,i=0,k=0,l=0;
	Parcial obj[5];
	Final obj2[5];
	
	do{
	cout<<"\t\n\tMENU\n\n";
	cout<<"1) Ingresar Alumno"<<endl;
	cout<<"2) Ingresar Calificaciones"<<endl;
	cout<<"3) Ver"<<endl;
	cout<<"\nSelecione una opcion: ";
	cin>>opcion;
		switch(opcion){
			case 1:
				obj[i].asignar();
				i++;
				system("cls");
				break;
			case 2:
				obj[k].usar_asig();
				k++;
				system("cls");
				break;
			case 3:
				cout << "\nNombre---------cal1--------------cal2----------Boleta---------------Semestre\n";
				for(int j=0; j<i; j++){
                    obj[j].ver();}
				l++;
				break;
			}
			
	cout<<"\nQuieres hacer otra cosa?\n 1)Si\n 2)No\n";
	cout<<": ";
	cin>>letra;
	}while(letra==1);
} 
