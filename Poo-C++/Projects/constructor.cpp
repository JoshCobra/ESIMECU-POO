#include <iostream>
using namespace std;

class Entero{
	int m,n;
	
	public:
		Entero(int, int);
		Entero();
		Entero (int);
		
	void mostrar(){
		cout<<"\n m="<<m<<"\t n="<<n<<endl;}
		
		};
		
		Entero::Entero(int x, int y){
		    m=x;n=y;}
		
		Entero::Entero(){
			m=0;n=0;}
			
		Entero::Entero(int x){
			m=0;n=x;}
			

int main(){
	
	Entero e1(4,5),p,r(5),h(8);
	Entero obj=Entero(6,7);
	
	Entero q=Entero();
	
	cout<<"\n --------RESULTADOS-------"<<endl;
	e1.mostrar();
	obj.mostrar();
	p.mostrar();
	q.mostrar();
	r.mostrar();
	h.mostrar();
	
	return 0;

}