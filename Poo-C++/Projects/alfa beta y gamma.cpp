#include <iostream>

using namespace std;

class alfa{
	int x;
	
	public:
		alfa(int i){
			x=i;
			cout<<"alfa consturido"<<endl;}
	void ver(){
		cout<<"x: "<<x<<endl;}
};

class beta{
	int p,q;
	
	public:
		beta(int a, int b):p(a),q(b+p){
		cout<<"beta construido"<<endl;}
	void ver(){
		cout<<"p: "<<p<<" q: "<<q<<endl;}	
};

class gamma:public beta, public alfa{
	int u, v;
	
	public:
		gamma(int a, int b, int c):alfa(a*5), beta(c,c), u(a){
			v=b;
			cout<<"gamma construido"<<endl;}
	void ver(){
		cout<<"u: "<<u<<" v: "<<v<<endl;}
};

int main(){
	gamma g(3,4,6);
	
	g.alfa::ver();
	g.beta::ver();
	g.ver();
	
	return 0;
}