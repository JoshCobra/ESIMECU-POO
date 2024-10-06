#include <iostream>

using namespace std;

class Ejemplo{
	int a,b;
	
	public:
		Ejemplo(int i, int j):a(i),b(j*2){
		}
		void ver();
};

void Ejemplo::ver(){
	cout<<"a: "<<a<<" y b: "<<b<<endl;}
	
int main(){
	
	Ejemplo obj (2,10);
	obj.ver();
	return 0;
	
}

