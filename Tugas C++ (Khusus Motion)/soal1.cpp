#include <iostream>
#include <iomanip>
using namespace std;


void tukar(int& a, int& b){ int temp=a; a=b; b=temp; }
void tukar(char& a, char& b){ char temp=a; a=b; b=temp; }
void tukar(double& a, double& b){ double temp=a; a=b; b=temp; }
void tukar(bool& a, bool& b){ bool temp=a; a=b; b=temp; }
void tukar(string& a, string& b){ string temp=a; a=b; b=temp; }

int main() {
    
    int n;
    char a;
    
    cin>>n;
    for(int i=0;i<n;i++){
        cin >>a;
        switch (a){
            case 'i':{
                int b, c;
                cin>>b>>c;
                tukar(b,c);
                cout << b <<" "<<c<<endl;
                break;}
                
            case 'c':{
                char b, c;
                cin>>b>>c;
                tukar(b,c);
                cout << b <<" "<<c<<endl;
                break;}
                
            case 'd':{
                double b, c;
                cin>>b>>c;
                tukar(b,c);
                cout << fixed << setprecision(1);
                cout << b <<" "<<c<<endl;
                break;}

            case 'b':{
                bool b, c;
                cin>>b>>c;
                tukar(b,c);
                cout << b <<" "<<c<<endl;
                break;}

            case 's':{
                string b, c;
                cin>>b>>c;
                tukar(b,c);
                cout << b <<" "<<c<<endl;
                break;}
        } 
    }

    return 0;
}
