#include<iostream>
using namespace std;
#define MAX 100

void leeCadena(int cant,int n[])
{
    int i;
    for(i=0;i<cant;i++)
    {
        cout<<"Ingresa elemento en A["<<i<<"] : ";
        cin>>n[i];
    }
     
}
 
void muestraCadena(int cant,int n[])
{
    int i;
    for(i=0;i<cant;i++)
    {
        cout<<"A["<<i<<"] : "<<n[i]<<endl;
    }
}
 
int leeCantidadElem()
{
    int n;
    do{
        cout<<"Cantidad de elementos a ingresar: ";cin>>n;
            if(n<=0)
                cout<<"...No seas payaso(a), ingresa una cantidad correcta: "<<endl;
            if(n>MAX)
                cout<<"...La cantidad maxima permitida es "<<MAX<<" : "<<endl;
    }while(n<=0 || n>MAX);
    return n;
}
 
int elegirEvento(int cant,int A[])
{
Opciones:
    int i,k,elem,opt;
    cout<<"1. Insertar elemento: "<<endl;
    cout<<"2. Eliminar elemento: "<<endl;
    cout<<"3. Agregar elemento: "<<endl;
    cout<<"4. Buscar elemento: "<<endl;
    cout<<"Elija una opcion 1 , 2 , 3 o 4: ";cin>>opt; 
    switch(opt)
    {
        case 1:
                {
                    cout<<"\t>>Que elemento desea insertar: ";cin>>elem;
                    do{
                    cout<<"\t>>En que posicion desea insertar...de [0] hasta ["<<cant-1<<"]: ";cin>>k;
                        if(k>(cant-1)||k<0)
                            cout<<">>Ingrese una posicion valida!!!"<<endl;
                    }while(k>(cant-1)||k<0);
                    cant++;
                    for(i=cant-1;i>=k;i--)
                    {
                        A[i+1]=A[i];
                        if(k==i)
                        A[k]=elem;      
                    }
                }break;
 
        case 2: 
                {
                    do{
                    cout<<"\t>>Que posicion desea eliminar...de [0] hasta ["<<cant-1<<"]: ";cin>>k;
                    if(k>(cant-1)||k<0)
                            cout<<">>Ingrese una posicion valida!!!"<<endl;
                    }while(k>(cant-1)||k<0);
                    for(i=k;i<cant;i++)
                    {
                        A[i]=A[i+1];
                    }
                        cant--;
                }break;
 
        case 3:
                {
                    for(i=0;i<1;i++)
                    {
                        cout<<"\t>>Que elemento desea agregar : ";cin>>elem;
                    Agregar:
                        cant++;
                        A[cant-1]=elem;         
                    }
                }break;
         
        case 4:
                {
                     
                    cout<<"\t>>Que elemento desea buscar: ";cin>>elem;
                    for(i=0;i<cant;i++)
                    {
                        if(A[i]==elem)
                        {
                            cout<<"\t>>El elemento buscado se encuentra en: A["<<i<<"]"<<endl;
                            //Añandir el elemento al final de arreglo
                            cout<<"\t>>El elemento se agregara al final"<<endl;
                        goto Agregar;
                        }
                        else
                        {
                            if(i==cant-1)
                            {
                            cout<<"\t>>No se encuetra el elemento que busca!!!"<<endl;
                            cout<<"\t>>Puede confirmarlo viendolo Ud. mismo!!!"<<endl;
                            }
                        }   
                    }
 
                }break;
        default:system("cls");cout<<"No existe esa opcion, vuelva a intentar: "<<endl;goto Opciones;break;
 
    }
 
return cant;
}
 
int main()
{
    int c;
    char opt;
    int n[MAX]; 
    cout<<"\t\t\tAGREGAR 2 ELEMENTOS AL FINAL"<<endl;
    c=leeCantidadElem();
    leeCadena(c,n);
    do{
    c=elegirEvento(c,n);
    muestraCadena(c,n);
    cout<<"Desea realizar otra operacion!!!... S/s, caso contrario pulse otra tecla: ";cin>>opt;
    }while(opt=='s'||opt=='S');
}