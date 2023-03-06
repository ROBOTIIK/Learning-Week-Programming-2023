#include <iostream>
#include <vector>
#include "Robot.h"
using namespace std;

int n, x, y;
vector<int>jumlah;

int main(){
    cin >> n;
    jumlah.push_back(n);
    Robot tes;
    for (int i = 0; i < n; i++){
        cin >> x; cin >> y;
        tes.setKoordinat(x, y);
    }
        
    for (int i = 0; i < n; i++){
        jumlah[i];
        if (x == 0 && y == 0){
            cout << "PUSAT\n";
        }else if (x == 0 && y > 0){
            cout << "UTARA\n";
        }else if (x > 0 && y == 0){
            cout << "TIMUR\n";
        }else if (x == 0 && y < 0){
            cout << "SELATAN\n";
        }else if (x < 0 && y == 0){
            cout << "BARAT\n";
        }else if (x == 0 && y == 0){
            cout << "PUSAT\n";
        }else if (x > 0 && y > 0){
            cout << "TIMUR LAUT\n";
        }else if (x > 0 && y < 0){
            cout << "TENGGARA\n";
        }else if (x < 0 && y < 0){
            cout << "BARAT DAYA\n";
        }else if (x < 0 && y > 0){
            cout << "BARAT LAUT\n";
        }
    }
        tes.cetak();
    
    
    return 0;
}
