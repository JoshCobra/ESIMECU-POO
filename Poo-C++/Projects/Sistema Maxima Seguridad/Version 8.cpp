#include <iostream>
using namespace std;

class datos{

	string nombre;
	string pais;
    int edad;
    
	
	public:
		
	void asigna(){
            cout<<"Escriba el Nombre del Recluso: ";
            cin>>nombre;
            cout<<"Ingrese Pais de residencia del Recluso: ";
            cin>>pais;
		    cout<<"Escriba Edad del Recluso: ";
		    cin>>edad;
			cout<<"\n\t\t**Datos Registrados**\n"; }
		
		int obt_edad(){
			return edad;}
			
		string obt_nombre(){
			return nombre;}
		
		string obt_pais(){
			return pais;}
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
            if(hrs < 24, hrs !=0){
            	cout<<"Hrs "<<hrs<<"/"<<"Escriba Minutos (00): ";	
                cin>>min;
				}else{
					cout<<"\t\t**Datos no Permitidos**";
					op=1;}
                if(min < 60, min !=0){
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
			cout<<"\nIngresa tipo de sangre: ";
			cin>>sangre;
			cout<<"Ingresa si padece alguna enfermedad: ";
			cin>>enfe;
		}
};

class registro:public datos, public fecha, public medic {
	
	int no;
	
	public:
		void ingresar(){
			cout<<"\n\tINGRESA LOS DATOS";
	    	cout<<"\nAsigna No. al Recluso: ";
	    	cin>>no;
	    	asigna();
	    	cout<<"\nIngrese Fecha y Hora de Ingreso del Recluso: ";
	    	asignaW();
	    	cout<<"\nIngresa Datos Medicos";
	    	asignaM();}
};

int main(){
	
	registro r[5];
	int i=0, j=0;
    int op,op1;
    
    do {
        cout<<"\t\n\tMenu\n\n";
        cout<<"1.Registrar recluso "<<endl;
        cout<<"2.Registra Fecha "<<endl;
        cout<<"3.Ver Datos "<<endl;
        cout<<"4.Salir "<<endl;
        cout<<"Escoja una opcion: ";
        cin>>op;
        switch(op) {
            case 1:
            	r[i].ingresar();
            	i++;
            	system("cls");
            break;
            case 2:

                i++;
            break;
            case 3:

            	i++;
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
