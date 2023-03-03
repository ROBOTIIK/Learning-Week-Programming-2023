#include <iostream>
#include <stdlib.h>
#include <string>
#include <bits/stdc++.h>
#include <sstream>
#include <iomanip>

using namespace std;

void tukari(int *a, int *b){
    int c = *a;
    *a = *b;
    *b = c;
}
void tukarc(char *a, char *b){
    char c = *a;
    *a = *b;
    *b = c;
}
void tukard(double *a, double *b){
    double c = *a;
    *a = *b;
    *b = c;
}
void tukarb(bool *a, bool *b){
    bool c = *a;
    *a = *b;
    *b = c;
}
void tukars(string *a, string *b){
    string c = *a;
    *a = *b;
    *b = c;
}

int main(){
    int n;
    cin >> n;
    char type[n];
    string hasil[n];

    //panggil stream temp perubah type
    stringstream ss;

    for (int i = 0; i < n; i++)
    {
        //temp data
        string z, f;
        //input
        cin >> type[i];
        switch (type[i])
        {
        case 'i':
        {
            int x, y;
            cin >> x >> y;
            tukari(&x,&y);
            //parsing data
            ss << x;
            ss >> z;
            ss.clear();
            ss << y;
            ss >> f;
            hasil[i] = z + " " + f;
        }
            break;
        case 'c':
        {
            char x, y;
            cin >> x >> y;
            tukarc(&x,&y);
            ss << x;
            ss >> z;
            ss.clear();
            ss << y;
            ss >> f;
            hasil[i] = z + " " + f;
        }
            break;
        case 'd':
        {
            double x, y;
            cin >> x >> y;
            tukard(&x,&y);
            ss << fixed << setprecision(1) << x; //beri nilai belkg koma
            ss >> z;
            ss.clear();
            ss << fixed << setprecision(1) << y;
            ss >> f;
            hasil[i] = z + " " + f;
        }
            break;
        case 'b':
        {
            bool x, y;
            cin >> x >> y;
            tukarb(&x,&y);
            ss << x;
            ss >> z;
            ss.clear();
            ss << y;
            ss >> f;
            hasil[i] = z + " " + f;
        }
            break; 
        case 's':
        {
            string x, y;
            cin >> x >> y;
            tukars(&x,&y);
            hasil[i] = x + " " + y;
        }
            break; 
        default:
            i--;
            break;
        }
        
        ss.clear();
    }

    for (int j = 0; j < n; j++)
    {
        cout << endl << hasil[j];
    }
    
    return 0;
}