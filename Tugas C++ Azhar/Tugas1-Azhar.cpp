#include <iostream>
#include <vector>
using namespace std;

int n, f, g;
char i, j;
double k, l;
bool m, h;
string o, p;
vector<char> pilihan;


void cetak();
void tukar (int& b, int& c){
    int temp = b;
    b = c;
    c = temp;
}

void tukar (char& b, char& c){
    char temp = b;
    b = c;
    c = temp;
}

void tukar (double& b, double& c){
    double temp = b;
    b = c;
    c = temp;
}

void tukar (bool& b, bool& c){
    bool temp = b;
    b = c;
    c = temp;
}

void tukar (string& b, string& c){
    string temp = b;
    b = c;
    c = temp;
}

int main(){
    cin >> n;
    if (n >= 1 && n <= 10){
        for (int z = 0; z < n; z++){
        char a;
        cin >> a;
        pilihan.push_back(a);
        switch (a){
            case 'i':
                cin >> f; cin >> g;
                tukar(f, g);
                break;
            case 'c':
                cin >> i; cin >> j;
                tukar(i, j);
                break;
            case 'd':
                cin >> k; cin >> l;
                tukar(k, l);
                break;
            case 'b':
                cin >> m; cin >> h;
                tukar(m, h);
                break;
            case 's':
                cin >> o; cin >> p;
                tukar(o, p);
                break;
            }
        }
    }else{
        cout << "Angka harus antara 1 - 10" << endl;
        return 1;
    }
    for (int q = 0; q < n; q++){
        switch (pilihan[q]){
            case 'i':
                cout<< f<< " " << g <<endl;
                break;
            case 'c':
                cout << i<< " " << j <<endl;
                break;
            case 'd':
                cout<< k<< " " << l <<endl;

                break;
            case 'b':
                cout<< m << " " << n <<endl;
                break;
            case 's':
                cout<< o << " " << p <<endl;
                break;
            }
    }
    
    return 0;
}