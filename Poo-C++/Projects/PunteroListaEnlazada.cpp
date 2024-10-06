#include <iostream>
using namespace std;

class NODO{
	public:
		int info;
		NODO *sig;
		NODO(){
			sig=NULL;
			info=0;
		}
};

int main(){
	
	NODO *q,*p;

	int op,op1;
	int i;
    
    do{
        cout<<"\t\n\tMenu\n\n";
        cout<<"1.Ingresar"<<endl;
        cout<<"2.Ver Datos"<<endl;
        cout<<"3.Buscar"<<endl;
        cout<<"4.Salir "<<endl;
        cout<<"Escoja una opcion: "<<endl;
        cin>>op;
        
        switch(op){
            case 1:
            	for(i=0; i<5; i++){
		        q= new NODO;
		        cout<<"Ingrese dato: ";
		        cin>>q->info;
		
		        q->sig = p;
	         	p=q;}
            break;
            case 2:   	
	         	cout<<"\nDatos ingresados: ";
            	while (q!= NULL){
		        cout<<q->info;
		        q=q->sig;}
		    break;
            case 3:       		
	            int buscar;
	            cout<<"Ingrese el dato a buscar: ";
	            cin>>buscar;
	            while(q!=NULL){
		        if(q->info==buscar){
		        cout<<"\nEncontrado";
		        q=q->sig;
				}else{
					cout<<"\nNo Encontrdao"<<endl;}break;}
            break;
            case 4:
                cout<<"\t\n\tSALIENDO\n\n";
                return 0;
            break;
            default:
                cout<<"\t\n\tError de opcion\n\n";
            break;
        }
        cout<<"\nDesea regresar al menu\n"<<endl;
        cout<<"1.SI/2.NO"<<endl;
        cin>>op1;
    }while (op1==1);
 
    return 0;
}
