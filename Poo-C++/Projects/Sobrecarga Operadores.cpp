#include <iostream>
using namespace std;

class Ejemplo{
	float x,y;
	
	public:
		Ejemplo(float xx, float yy){
			x=xx;    y=yy;
		}
		Ejemplo(){
		x=0;	y=0;
		}
		
		friend Ejemplo operator+(Ejemplo,Ejemplo);
		friend Ejemplo operator-(Ejemplo,Ejemplo);
		friend Ejemplo operator-(Ejemplo);
		void Ver();
};

void Ejemplo::Ver(){
	cout<<x<<","<<y<<endl;
}

Ejemplo operator-(Ejemplo o){
	return Ejemplo (-o.x,-o.y);
	
}

Ejemplo operator+(Ejemplo a, Ejemplo b){
	Ejemplo aux;
	aux.x=a.x+b.x;
	aux.y=a.y+b.y;
	return aux;
}

Ejemplo operator-(Ejemplo a, Ejemplo b){
	return Ejemplo (a.x-b.x,a.y-b.y);
}

int main(){
	
	Ejemplo a(3,4),b(5,2),c,d;
	
	a.Ver();
	b.Ver();
	c=a+b;
	c.Ver();
	c=a-b;
	c.Ver();
	d=-c;
	d.Ver();
	
	return 0;
	
}