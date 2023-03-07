#include <iostream>

using namespace std;

void tukar(int& a, int& b){
	int temp = a;
	a = b;
	b = temp;
}

void tukar(char& a, char& b){
	char temp = a;
	a = b;
	b = temp;
}

void tukar(double& a, double& b){
	double temp = a;
	a = b;
	b = temp;
}

void tukar(bool& a, bool& b){
	bool temp = a;
	a = b;
	b = temp;
}

void tukar(string& a, string& b){
	string temp = a;
	a = b;
	b = temp;
}

int main(){
	
//	int a = 1;
//	int b = 2;
//	tukar(a, b);
//	cout << a << ' ' << b;
	
//	return 0;

	char a;
	int n;
	
	cin >> n;
	
	while (n--)
	{
		cin >> a;
		switch(a)
		{
			case 'i':
			{
				int b,c;
				cin >> b >> c;
				tukar(b,c);
				cout << b << " " << c << endl;
				break;
			}
			case 'c':
			{
				char b,c;
				cin >> b >> c;
				tukar(b,c);
				cout << b << " " << c << endl;
				break;
			}
			case 'd':
			{
				double b,c;
				cin >> b >> c;
				tukar(b,c);
				cout << b << " " << c << endl;
				break;
			}
			case 'b':
			{
				bool b,c;
				cin >> b >> c;
				tukar(b,c);
				cout << b << " " << c << endl;
				break;
			}
			case 's':
			{
				string b,c;
				cin >> b >> c;
				tukar(b,c);
				cout << b << " " << c << endl;
				break;
			}
			
		}
	}	
	
	return 0;
	
}

