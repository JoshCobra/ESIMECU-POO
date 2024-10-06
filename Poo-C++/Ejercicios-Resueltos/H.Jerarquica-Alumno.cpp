//SISTEMA DE MAXIMA SEGURIDAD

#include <iostream>
#include <stdlib.h>

using namespace std;


int GetIndex(int tam){
    bool error;
    int del;
    string aux;

    do{
        cin>>aux;
        error=false;
        for(int i=0;i<aux.length();i++){
            if(!isdigit(aux[i])){
                error=true;
                break;
            }
        }
        if(!error){
            del=atoi(aux.c_str());
            if(del > tam || del < 0){
                error=true;
             }
        }
        if(error)
            cout<<"Dato incorrecto."<<endl<<"Vuelve a intentarlo: ";
    }while(error);

    return del;
}

class guardar{
	
	public:
		
	guardar(int tam, string arr[]){
    char res;
    cout << "Al ingresar nuevos datos se perderan datos anteriores, desea continuar s/n: " << endl;
    cin>>res;
    res=toupper(res);

    if(res=='S'){
        for(int i=0;i<tam; i++){
            if(arr[i]==""){
                cout<<"Ingrese valor para la posicion " << i << endl;
                cin>>arr[i];
            }
        }
    }
}
};

class calif{
	
	public:
		
	calif(int tam, string arr[]){
    char res;
    cout << "Al ingresar nuevos datos se perderan datos anteriores, desea continuar s/n: " << endl;
    cin>>res;
    res=toupper(res);

    if(res=='S'){
        for(int i=0;i<tam; i++){
            if(arr[i]==""){
                cout<<"Ingrese valor para la posicion " << i << endl;
                cin>>arr[i];
            }
        }
    }
}
};

class ver{
	
	public:
		
	ver(int tam, string arr[]){
    for(int i=0; i<tam;i++){
        if(arr[i]!=""){
            cout<<i<<" "<< arr[i] << endl;
        }else{
            cout<<i<<" vacio"<<endl;
        }
    }
}
};

class borrar{
	
	public:
		
	borrar(int tam,string arr[]){
    int del;

    for(int i=0;i<tam;i++){
        cout<<i<<" "<<arr[i]<<endl;
    }
    cout << "Que nombre de entrada desea borrar: "<< endl;

    del=GetIndex(tam);

    if(arr[del]==""){
        cout<<"Registro vacio"<<endl;
    }else{
        arr[del]="";
        cout<<"Registro Borrado"<<endl;
    }
}
};

class buscar{
	
	public:
		
	buscar(int tam,string arr[]){
    string bus;
    bool encontrado=false;

    cout<<"Introduzca el codigo a buscar: ";
    cin>>bus;

    for(int i=0;i<tam;i++){
        if(arr[i]==bus){
            cout<<arr[i] << " encontrado en la posicion " << i << endl;
            encontrado=true;
        }
    }
    if(!encontrado)
        cout<<"Codigo no encontrado"<<endl;
}
};


int menu(int tam, string arr[]){
	
    char ent;
    cout << "Eliga la accion que quiera realizar:" << endl << "A.- Ingresar" << endl << "B.- Ingresar Calificacion" << endl << "C.- Ver" << endl << "D.- Buscar" << endl << "E.- Borrar" << endl << "F.- Salir" << endl;
    cout<<"Introduzca una opcion: ";
    do{
        cin >> ent;
        ent=toupper(ent);
        if(ent<'A' || ent>'F')
            cout << "Entrada no valida" << endl << "Intente de nuevo: ";
    }while(ent<'A' || ent>'F');

    switch(ent){
        case 'A':
            system("cls");
            guardar(tam,arr);
            system("pause");
            break;
        case 'B':
        	system("cls");
        	calif(tam,arr);
        	system("pause");
        	break;
        case 'C':
            system("cls");
            ver(tam,arr);
            system("pause");
            break;
        case 'D':
            system("cls");
            buscar(tam,arr);
            system("pause");
            break;
        case 'E':
            system("cls");
            borrar(tam,arr);
            system("pause");
            break;
        case 'F':
        	break;
    }
    system("cls");
    return ent;
}

int main(){
	
    const int tam=15;
    int op;
    string arr[tam];

    for(int i=0;i<tam;i++)
        arr[i]="";
    do{
        op=menu(tam,arr);
    }while(op!='F');
}