#include <iostream>

using namespace std;

class Datos{

		string nombre;
		int tel;
		
	public:
		void asignar(){
	    cout<<"Ingresa el nombre: ";
	    cin>>nombre;
	    cout<<"Ingresa el numero de telefono: ";
	    cin>>tel;}
	        
		int obt_tel(){
			return tel;}
				
		string obt_nom(){
			return nombre;}	
};

class Alumno:private Datos{
	
		int n_bol,sem;
		
	public:
		
	    void usar_asig(){
	    cout<<"Ingresa el numero de boleta: ";
	    cin>>n_bol;
	    cout<<"Ingresa el semestre: ";
	    cin>>sem;
	    asignar();}
	
		void ver();
};

void Alumno::ver(){
	cout<<obt_nom()<<"\t\t"<<obt_tel()<<"\t\t"<<n_bol<<"\t\t"<<sem<<"\n";
}

class Docente:public Datos{
	private:
		string carrera,turno;
		int N_emp;
	public:
		void asignar_();
		void ver_();
};

void Docente::asignar_(){
	asignar();
	cout<<"Ingreas la carrera: ";
	cin>>carrera;
	cout<<"Ingresa el turno: ";
	cin>>turno;
	cout<<"Ingrese el numero de empleado: ";
	cin>>N_emp;
}

void Docente::ver_(){
	cout<<obt_nom()<<"\t\t"<<obt_tel()<<"\t\t"<< carrera<<"\t\t"<< turno<<"\t\t"<<N_emp<<"\n";
}

class Administrador:protected Datos{
	private:
		string puesto,turno;
	public:
		void usar();
		void Ver_();
};

void Administrador::usar(){
	asignar();
	cout<<"Ingrese el puesto: ";
	cin>>puesto;
	cout<<"Ingrese el turno: ";
	cin>>turno;
}

void Administrador::Ver_(){
	cout<<obt_nom()<<"\t\t"<<obt_tel()<<"\t\t"<< puesto<<"\t\t"<< turno<<"\n";
}

main(){
	
	int opcion,letra,i=0,k=0,l=0;
	Alumno obj[5];
	Docente obj1[5];
	Administrador obj2[5];
	
	do{
	cout<<"\t\n\tMENU\n\n";
	cout<<"1) Ingresar Alumno"<<endl;
	cout<<"2) Ingresar Docente"<<endl;
	cout<<"3) Ingresar Administrador"<<endl;
	cout<<"4) Ver Alumnos"<<endl;
	cout<<"5) Ver Docentes"<<endl;
	cout<<"6) Ver Administrativos"<<endl;
	cout<<"\nSelecione una opcion: ";
	cin>>opcion;
		switch(opcion){
			case 1:
				obj[i].usar_asig();
				i++;
				break;
			case 2:
				obj1[k].asignar_();
				k++;
				break;
			case 3:
				obj2[l].usar();
				l++;
				break;
			case 4:
			cout << "\nNombre-------Telefono--------------Boleta---------------Semestre\n";
				for(int j=0; j<i; j++){
                    obj[j].ver();
				}
				break;
			case 5:
				cout << "\nNombre----Telefono----Carrera------------Turno---------------No.empleado\n";
				for(int j=0; j<k; j++){
                    obj1[j].ver_();
				}
				break;
			case 6:
				cout << "\nNombre---------Telefono-----------Carrera-------------------Turno\n";
				for(int j=0; j<l; j++){
                    obj2[j].Ver_();
				}
				break;	
		}
	cout<<"\nQuieres hacer otra cosa?\n 1)Si\n 2)No\n";
	cout<<": ";
	cin>>letra;
	}while(letra==1);
} 