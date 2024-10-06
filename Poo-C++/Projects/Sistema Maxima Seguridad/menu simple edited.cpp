
//SISTEMA DE MAXIMA SEGURIDAD

#include <iostream>
#include <conio.h>
#include <stdio.h>


using namespace std;
 
void guardar(int cant, string arr[]){
	int no;
    char res;
    cout << "Al ingresar nuevos datos se perderan datos anteriores, desea continuar s/n: " << endl;
    cin>>res;
    res=toupper(res);

    if(res=='S'){
        for(int i=0;i<cant; i++){
            if(arr[i]==""){
            	cout<<"Ingrese Numero del recluso: ";
            	cin>>no;
                cout<<"Ingrese Nombre del recluso " << no << endl;
                cin>>arr[i];
            }
        }
    }
}

void ver(int cant, string arr[]){
	cout<<"\tNumero--------------Nombre---------------------Entrada-Fecha----Hora----------------Sentencia-------------\n";
    for(int i=0; i<cant;i++){
        if(arr[i]!=""){
            cout<<i<<" "<< arr[i] << endl;
        }else{
        }
    }
    cout<<"\n\n\t----------------------------------------------------------------------------------------------------------\n";
}

int GetIndex(int cant){
    bool error;
    char del;
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
            if(del > cant || del < 0){
                error=true;
             }
        }
        if(error)
            cout<<"Dato no esta en el registro."<<endl<<"Vuelve a intentarlo: ";
    }while(error);

    return del;
}

void borrar(int cant,string arr[]){
    char del;

    for(int i=0;i<cant;i++){
        cout<<i<<" "<<arr[i]<<endl;
    }
    cout << "Que datos de entrada desea borrar: "<< endl;

    del=GetIndex(cant);

    if(arr[del]==""){
        cout<<"Registro vacio"<<endl;
    }else{
        arr[del]="";
        cout<<"Registro Borrado"<<endl;
    }
}

void buscar(int cant,string arr[]){
    string bus;
    bool encontrado=false;

    cout<<"Introduzca el codigo a buscar: ";
    cin>>bus;

    for(int i=0;i<cant;i++){
        if(arr[i]==bus){
            cout<<arr[i] << " encontrado en la posicion " << i << endl;
            encontrado=true;
        }
    }
    if(!encontrado)
        cout<<"Codigo no encontrado"<<endl;
}

int menu(int cant, string arr[]){
	
    char ent;
    cout << "Eliga la accion que quiera realizar:" << endl << "A.- Ingresar" << endl << "B.- Ver" << endl << "C.- Buscar" << endl << "D.- Borrar" << endl << "E.- Salir" << endl;
    cout<<"Introduzca una opcion: ";
    do{
        cin >> ent;
        ent=toupper(ent);
        if(ent<'A' || ent>'E')
            cout << "Entrada no valida" << endl << "Intente de nuevo: ";
    }while(ent<'A' || ent>'E');

    switch(ent){
        case 'A':
            system("cls");
            guardar(cant,arr);
            system("pause");
            break;
        case 'B':
            system("cls");
            ver(cant,arr);
            system("pause");
            break;
        case 'C':
            system("cls");
            buscar(cant,arr);
            system("pause");
            break;
        case 'D':
            system("cls");
            borrar(cant,arr);
            system("pause");
            break;
        case 'E':
        	break;
    }
    return ent;
}

int main(){
	
    int cant=1;
    int op;
    string arr[cant];

    for(int i=0;i<cant;i++)
        arr[i]="";
    do{
        op=menu(cant,arr);
    }while(op!='F');
    
    getch();
}