#include <iostream>
using namespace std;

class datos{

	string nombre;
	string estado;
    int edad;
    
	
	public:
		
	void asigna(){
            cout<<"Escriba el Nombre del Recluso: ";
            cin>>nombre;
            cout<<"Ingrese Estado de residencia del Recluso: ";
            cin>>estado;
		    cout<<"Escriba Edad del Recluso: ";
		    cin>>edad;
			cout<<"\n\t\t**Datos Registrados**\n"; }
		
		int obt_edad(){
			return edad;}
			
		string obt_nombre(){
			return nombre;}
		
		string obt_estado(){
			return estado;}
};

class hrs{
	
	int hrs, min;
	
	public:
	
	
	void asignaHrs(){
		
	cout<<"Digite la hora formato 24hrs: ";
	cin>>hrs;
	while(hrs>24){
		cout<<"\nDigite una *HORA VALIDA*: ";
		cin>>hrs;
		if(hrs>24){
			cout<<"\n\t*Dato no Valido*";}
	   }
	   
	cout<<"Digite Minutos (Maximo 60): ";
	cin>>min;
	while(min>60){
		cout<<"\nDigite *MINUTOS VALIDOS*: ";
		cin>>min;
		if(min>60){
			cout<<"\n\t*Dato no Valido*";}
	   }
	}
};

class fecha:private hrs{
	
	int dia, mes, anio;
		
	public:
	
	void asignaF(){
	cout<<"Digite dia formato (00): ";
	cin>>dia;
	while(dia>31){
		cout<<"\nDigite un *DIA VALIDO*: ";
		cin>>dia;
		if(dia>31){
			cout<<"\n\t*Dato no Valido*";}
	}
	   
	cout<<"Digite Mes formato (00): ";
	cin>>mes;
	while(mes>12){
		cout<<"\nDigite *MES VALIDO*: ";
		cin>>mes;
		if(mes>12){
			cout<<"\n\t*Dato no Valido*";}
	}	
	   	
	cout<<"Digite Anio formato (0000): ";
	cin>>anio;
	while(anio<2000){
		cout<<"\nDigite *ANIO VALIDO*: ";
		cin>>anio;
		if(anio<2000){
			cout<<"\n\t*Dato no Valido*";}
	}	   
			asignaHrs();					
		}		
		
		int obt_dia(){
			return dia;}
			
		int obt_mes(){
			return mes;}
		
		int obt_anio(){
			return anio;}
};
	
class medic{
	
	char sangre;
	char sign;
	string enfe;
	
	public:
		
		void asignaM(){
			cout<<"\nIngresa tipo de (sangre) 'espacio' (signo) en caso de tenerlo (+)(-) sin signo escribir 0: ";
			cin>>sangre;
			cout<<"Ingresa si padece alguna enfermedad (Si) o (No): ";
			cin>>enfe;
			cout<<"\n\t\t**Datos Registrados**\n";
		}
 		
		char obt_sangre(){
			return sangre;}
			
		char obt_sign(){
			return sign;}
		
		string obt_enfe(){
			return enfe;}
};

class registro:public datos, public fecha, public medic {
	
	public:
			int no;
			
		void ingresar(){
			cout<<"\n\tINGRESA LOS DATOS\n";
	    	cout<<"\nAsigna No. al Recluso: ";
	    	cin>>no;
	    	asigna();
	    	cout<<"\nIngrese Fecha y Hora de Ingreso del Recluso"<<endl;
	    	asignaF();
	    	cout<<"\nIngresa Datos Medicos";
	    	asignaM();}
	    	
	    void imprimir(){
	    	cout<<"\t     "<<no<<"\t\t "<<obt_nombre()<<"      "<<obt_estado()<<"\t\t"<<obt_mes()<<"/"<<obt_anio()<<"\t\t\t"<<obt_enfe()<<endl;
		}	
};

int main(){
	
	registro obj[5];
	int i=0, j=0, k=0;
	int dato;
  	char band = 'F';
    int op,op1;
    
    do {
        cout<<"\t\n\tMenu\n\n";
        cout<<"1) Registrar recluso"<<endl;
        cout<<"2) Ver Datos"<<endl;
        cout<<"3) Buscar Datos"<<endl;
        cout<<"4) Salir"<<endl;
        cout<<"Seleccione una opcion: ";
        cin>>op;
        switch(op){
            case 1:
            	obj[i].ingresar();
            	i++;
            	system("cls");
            break;
            case 2:
			    cout<<"\n\tNo.Recluso------Nombre-------Estado---------Mes/Anio de Ingreso--------Enfermedad\n";
				    for(int j=0; j<i; j++){
                        obj[j].imprimir();}            	
            break;
            case 3:			
            cout<<"\nIngresa el numero de recluso a buscar: ";
            cin>>dato;
            while( (band == 'F') && (j<5) ){
            	if(obj[j].no == dato){
            		band = 'V';
				}
				j++;
			}
			if(band == 'F'){
				cout<<"\n\t\t**Recluso no Registrado**\n";
			}
			else if (band == 'V'){
				cout<<"Se encontro el recluso en la posicion: "<<j-1;
				cout<<"\n\tNo.Recluso------Nombre-------Estado---------Mes/Anio de Ingreso--------Enfermedad\n";
				    for(int j=0; j<i; j++){
                        obj[j].imprimir();} 
				}
            break;
            case 4:
                cout<<"\t\n\tSALIENDO\n\n";
                return 0;
            break;
            default:
                cout<<"\t\n\tError de opcion\n\n";
            break;
        }
        cout<<"\nDesea regresar al menu"<<endl;
        cout<<"1.SI/2.NO"<<" :";
        cin>>op1;
        system("cls");
        
    }while (op1==1);
 
    return 0;
}
