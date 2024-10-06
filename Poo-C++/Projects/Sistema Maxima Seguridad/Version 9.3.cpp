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

class fecha{
	
		int dia=0, mes=0, anio=0, hrs=0, min=0;
		int op=0;
		
		public:
			
		void asignaW(){
			do{
				asignaF();
			}while(op==1);
		}	
	
		void asignaF(){
            cout<<"\nEscriba Dia(00): ";
            cin>>dia;
            if(dia < 31){
            	cout<<"Dia "<<dia<<"/"<<"Escriba Mes(00): ";	
                cin>>mes;
				}else{
					cout<<"\t\t**Datos no Permitidos**";
					op=1;}
                if(mes < 13){
                	cout<<"Dia "<<dia<<"/"<<"Mes "<<mes<<"/"<<"Escriba Anio(0000): ";
                	cin>>anio;
					}else{
					cout<<"\t\t**Datos no Permitidos**";
					op=1;}
					
			cout<<"\nIngrese Hora y Min de entrada";
            cout<<"\nEscriba Hora (00): ";
            cin>>hrs;
            if(hrs < 24){
            	cout<<"Hrs "<<hrs<<"/"<<"Escriba Minutos (00): ";	
                cin>>min;
				}else{
					cout<<"\t\t**Datos no Permitidos**";
					op=1;}
                if(min < 60){
                	cout<<"\n\t\t**Datos Registrados**\n";
					}else{
					cout<<"\t\t**Datos no Permitidos**";
					op=1;}
		}		
		
		int obt_dia(){
			return dia;}
			
		int obt_mes(){
			return mes;}
		
		int obt_anio(){
			return anio;}
			
		int obt_hrs(){
			return hrs;}
			
		int obt_min(){
			return min;}
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
	
	int no;
	
	public:
		void ingresar(){
			cout<<"\n\tINGRESA LOS DATOS\n";
	    	cout<<"\nAsigna No. al Recluso: ";
	    	cin>>no;
	    	asigna();
	    	cout<<"\nIngrese Fecha y Hora de Ingreso del Recluso: ";
	    	asignaW();
	    	cout<<"\nIngresa Datos Medicos";
	    	asignaM();}
	    	
	    void imprimir(){
	    	cout<<"\t     "<<no<<"\t\t "<<obt_nombre()<<"      "<<obt_estado()<<"\t\t"<<obt_mes()<<"/"<<obt_anio()<<"\t\t\t"<<obt_enfe()<<endl;
		}
			
		void buscar(){
			
			int k=0;
			int dato;
  	    char band = 'F';
			
            cout<<"\nIngresa el numero de recluso a buscar: ";
            cin>>dato;
            while( (band == 'F') && (k<5) ){
            	if(no == dato){
            		band = 'V';
				}
				k++;
			}
			if(band == 'F'){
				cout<<"\n\t\t**Recluso no Registrado**\n";
			}
			else if (band == 'V'){
				cout<<"Se encontro el recluso en la posicion: "<<k-1;
				cout<<"\n\tNo.Recluso------Nombre-------Estado---------Mes/Anio de Ingreso--------Enfermedad\n";
				imprimir();}		
		}
};

int main(){
	
	registro obj[5];
	int i=0, j=0;
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
            	obj[j].buscar();
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
