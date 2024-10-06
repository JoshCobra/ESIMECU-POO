#include <iostream>
using namespace std;

class datos{

	string estado;
    int edad;
    
	
	public:
		
	void asigna(){
            cout<<"Ingrese Estado de residencia: ";
            cin>>estado;
		    cout<<"Escriba Edad: ";
		    cin>>edad;
	while(edad<18){
		cout<<"\n*Necesita ser mayor de edad para abrir una cuenta*: ";
		cin>>edad;
		if(edad>17){
			cout<<"\n\t*Datos Registrados Correctamente*";}
	   }
}
		
		int obt_edad(){
			return edad;}
		
		string obt_estado(){
			return estado;}
};

class registro:public datos{
	
	public:
			int no;
			float c;
			string nombre;
				
		void ingresar(){
			cout<<"\n\tINGRESA LOS DATOS\n";
            cout<<"Ingrese Nombre Titular de la cuenta: ";
            cin>>nombre;
	    	cout<<"\nAsigna No. a su cuenta: ";
	    	cin>>no;
	    	asigna();}
	    	
	    void imprimir(){
	    	cout<<"\t     "<<no<<"\t\t "<<nombre<<"\t\t          "<<obt_estado()<<endl;}
};


int main(){

	registro obj[5];
	int i=0, j=0, k=0;
	int dato;
  	char band = 'F';
    int op,op1;
    
    do {
        cout<<"\t\n\tMenu\n\n";
        cout<<"1) Registrar Cuenta"<<endl;
        cout<<"2) Ver Cuentas Registradas"<<endl;
        cout<<"3) Eliminar Cuenta"<<endl;
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
			    cout<<"\n\tNo. de Cuenta------Titular de Cuenta-------Estado de Residencia\n";
				    for(int j=0; j<i; j++){
                        obj[j].imprimir();}            	
            break;
            case 3:			
            cout<<"\nIngresa el numero de cuenta a eliminar: ";
            cin>>dato;
            while( (band == 'F') && (j<5) ){
            	if(obj[j].no == dato){
            		band = 'V';
				}
				j++;
			}
			if(band == 'F'){
				cout<<"\n\t\t**Cuenta no Registrada**\n";
			}
			else if (band == 'V'){
				cout<<"Se encontro el recluso en la posicion: "<<j-1;
				
				obj[5].no = 0;
				
			    cout<<"*Cuenta eliminada correctamente*";
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
