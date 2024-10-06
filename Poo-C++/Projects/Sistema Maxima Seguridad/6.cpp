#include <iostream>
using namespace std;

class registro{
	
	int no;
	char nombre[35];
    int edad;
	
	public:
		
	void asigna(){
		cout<<"\n\nEscriba el Numero de Recluso "<<": ";
        cin>>no;
        cout<<"Escriba el Nombre del Recluso "<<no<<": ";
        cin>>nombre;
		cout<<"Escriba Edad del Recluso: ";
		cin>>edad; }
		
		int obt_no(){
			return no;}
			
		string obt_nombre(){
			return nombre;}
			
		int obt_edad(){
			return edad;}
		
};

class fecha:public registro{
	
	int dia, mes, anio;
	int hrs,min;
	
	public:
		void registro(){
			int no=0;
			cout<<"\nIngrese el numero de recluso para asignar los datos: ";
			cin>>no;
			if (obt_no() == no){
				asignaF();
			}else{
				cout<<"\t\t**Recluso no registrado**\n";}
		}
		
		void asignaF(){
		cout<<"\n\nINGRESE FECHA DE INGRESO DEL RECLUSO";
        cout<<"\nEscriba Dia(00)  'espacio'  Mes(00)  'espacio'  Anio(0000): ";
        cin>>dia>>mes>>anio;
        cout<<"\nEscriba Hora de entrada(hrs)'espacio'(min): ";
		cin>>hrs>>min; }		
		
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

class ver:public fecha{
	
	public:
		void imprimir(){
		cout<<"\tNumero--------------Nombre---------------------Entrada-Fecha----Hora----------------Sentencia-------------\n";
		cout<<obt_no()<<"\t"<<obt_nombre()<<"\t"<<obt_edad()<<"\t"<<obt_dia()<<":"<<obt_mes()<<":"<<obt_anio()<<"\t"<<obt_hrs()<<":"<<obt_min();
        cout<<"\n\n\t----------------------------------------------------------------------------------------------------------\n";
		}
	};
	
class DatosM:public registro{
	
	char sangre;
	string enfe;
	
	public:
		void Dmedicos(){
			cout<<"INGRESA DATOS MEDICOS"<<endl;
			cout<<"Ingresa tipo de sangre: ";
			cin>>sangre;
			cout<<"Ingresa si padece alguna enfermedad: ";
			cin>>enfe;
		}
};


int main(){
	
	ver v[5];
	int i=0;
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
            	v[i].asigna();
            	i++;
            	system("cls");
            break;
            case 2:
                v[i].registro();
                i++;
            break;
            case 3:
            	v[i].imprimir();
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
    }while (op1==1);
 
    return 0;
}
