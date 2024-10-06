#include <iostream>
#include <conio.h>
using namespace std;

class Animal {
  public:
       void caminar() {
           cout << "Caminando en Animal" << endl;
       }
};

class Mamifero{
  public:
       void caminar() {
           cout << "Caminando en Mamifero" << endl;
       }    
};
 
class Perro:public Animal, public Mamifero { };

int main(){
	
    Perro dog;
    
    dog.Animal::caminar();
    dog.Mamifero::caminar();
}