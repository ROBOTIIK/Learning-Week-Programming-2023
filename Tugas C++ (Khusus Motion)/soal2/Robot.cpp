#include <iostream>
#include "Robot.h"

using namespace std;

void Robot::init(){
    int n, x, y;
    cin>>n;
    for (int i =0 ; i<n;i++){
        cin >> x >> y;
        arah(x, y);
        setArah(x,y);
    }
    akhir();
}

void Robot::arah(int x, int y){

    if(y==0){
        if(x>0){cout<<"TIMUR\n";}
        else if (x<0){cout<<"BARAT\n";}
    } else if(x==0){
        if(y>0){cout<<"UTARA\n";}
        else if (y<0){cout<<"SELATAN\n";}
    } else if(x>0){
        if(y>0){cout<<"TIMUR LAUT\n";}
        else if(y<0){cout<<"TENGGARA\n";}
    } else {
        if(y>0){cout<<"BARAT LAUT\n";}
        else{cout<<"BARAT DAYA\n";}
    }
}

void Robot::setArah(int x, int y){
    absis+=x; ordinat+=y;
}

void Robot::akhir(){
    cout << "KOORDINAT AKHIR: (" << absis << ", " <<ordinat <<")\n";
}