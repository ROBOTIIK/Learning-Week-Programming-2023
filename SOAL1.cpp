#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

void tukar(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void tukar(char& a, char& b) {
    char temp = a;
    a = b;
    b = temp;
}

void tukar(double& a, double& b) {
    double temp = a;
    a = b;
    b = temp;
}

void tukar(bool& a, bool& b) {
    bool temp = a;
    a = b;
    b = temp;
}

void tukar(string& a, string& b) {
    string temp = a;
    a = b;
    b = temp;
}

int main() {
    int n;
    cin >> n;

    while (n--) {
        char type;
        cin >> type;

        switch (type) {
            case 'i': {
                int a, b;
                cin >> a >> b;
                tukar(a, b);
                cout << a << ' ' << b << endl;
                break;
            }
            case 'c': {
                char a, b;
                cin >> a >> b;
                tukar(a, b);
                cout << a << ' ' << b << endl;
                break;
            }
            case 'd': {

                double a, b;
                cin >> a >> b;
                tukar(a, b);
                cout << fixed << setprecision(1) << a << " " << b << endl;
                break;
            }
            case 'b': {
                bool a, b;
                cin >> a >> b;
                tukar(a, b);
                cout << a << ' ' << b << endl;
                break;
            }
            case 's': {
                string a, b;
                cin >> a >> b;
                tukar(a, b);
                cout << a << ' ' << b << endl;
                break;
            }
        }
    }

    return 0;
}