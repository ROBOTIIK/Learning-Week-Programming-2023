#include <iostream>
#include <vector>
using namespace std;

int n, e, f;
char g, h;
double i, j;
bool k, l;
string m, o;
vector<char> input;


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
        for (int z = 0; z < n; z++){
        char a;
        cin >> a;
        input.push_back(a);
        switch (a){
            case 'i':
                cin >> e; cin >> f;
                tukar(e, f);
                break;
            case 'c':
                cin >> g; cin >> h;
                tukar(g, h);
                break;
            case 'd':
                cin >> i; cin >> j;
                tukar(i, j);
                break;
            case 'b':
                cin >> k; cin >> l;
                tukar(k, l);
                break;
            case 's':
                cin >> m; cin >> o;
                tukar(m, o);
                break;
            }
        }
    cout << "=============================="<< endl;
    for (int q = 0; q < n; q++){
        switch (input[q]){
            case 'i':
                cout<< e<< " " << f <<endl;
                break;
            case 'c':
                cout << g<< " " << h <<endl;
                break;
            case 'd':
                cout<< i<< " " << j <<endl;

                break;
            case 'b':
                cout<< k << " " << l <<endl;
                break;
            case 's':
                cout<< m << " " << o <<endl;
                break;
            }
    }
    
    return 0;
}