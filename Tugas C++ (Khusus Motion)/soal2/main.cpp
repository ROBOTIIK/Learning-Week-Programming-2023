#include<iostream>
#include "Robot.h"
using namespace std;

int main() {
    Robot R1;
    int n, x, y;
    
    cin>>n;
    for (int i =0 ; i<n;i++){
        cin >> x >> y;
        
        R1.arah(x, y);
        R1.setArah(x,y);
    }
    
    R1.akhir();
    
    return 0;
}
