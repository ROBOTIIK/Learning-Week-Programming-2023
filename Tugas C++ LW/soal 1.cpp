#include <iostream>
using namespace std;

int tukar(int &b, int &c) {
  int d = b; b = c ; c = d;
}
char tukar(char &b, char &c) {
  char d = b; b = c ; c = d;
}
double tukar(double &b, double &c) {
  double d = b; b = c ; c = d;
}
bool tukar(bool &b, bool&c) {
  bool d = b; b = c ; c = d;
}
string tukar(string &b, string &c) {
  string d = b; b = c ; c = d;
}

int main(){
	int n; cin >> n;

  for(int i=0;i<n;i++) {
    char a;cin >> a;

		switch(a){

			case 'i':{
				int a, b;
				cin >> a >> b;
				tukar(a,b);
				cout << a << " " << b << endl;
				break;
			}

			case 'c':{
				char a, b;
				cin >> a >> b;
				tukar(a,b);
				cout << a << " " << b << endl;
				break;
			}

			case 'd':{
				double a, b;
				cin >> a >> b;
				tukar(a,b);
				cout << a << " " << b << endl;
				break;
			}

			case 'b':{
				bool a, b;
				cin >> a >> b;
				tukar(a,b);
				cout << a << " " << b << endl;
				break;
			}

			case 's':{
				string a, b;
				cin >> a >> b;
				tukar(a,b);
				cout << a << " " << b << endl;
				break;
			}
			
		}
  }
}
