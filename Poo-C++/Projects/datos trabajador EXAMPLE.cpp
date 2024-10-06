#include <iostream>
using namespace std;

struct Fecha{
 int dia,mes,anio;
};

struct Persona{
 char nombre[20];
 int edad,peso;
 Fecha fecha;
}persona = {"Cindy",20,45,2,12,1997};

struct Empleado{
 Persona persona;
 int salario;
}trabajador = {"Steven",19,60,22,7,1998,1000};

int main(){
 cout <<"Persona: " <<persona.nombre;
 cout <<"\nEdad: " <<persona.edad;
 cout <<"\nPeso: " <<persona.peso;
 cout <<"\nDia nacimiento: " <<persona.fecha.dia;
 cout <<"\nMes nacimiento: " <<persona.fecha.mes;
 cout <<"\nAno nacimiento: " <<persona.fecha.anio;
 
 cout <<"\n\n----------Trabajador----------" <<endl;
 
 cout <<"\nTrabajador: " <<trabajador.persona.nombre;
 cout <<"\nEdad: " <<trabajador.persona.edad;
 cout <<"\nPeso: " <<trabajador.persona.peso;
 cout <<"\nDia nacimiento: " <<trabajador.persona.fecha.dia;
 cout <<"\nMes nacimiento: " <<trabajador.persona.fecha.mes;
 cout <<"\nAno nacimiento: " <<trabajador.persona.fecha.anio;
 cout <<"\nSalario: " <<trabajador.salario;
   
   return 0;
}