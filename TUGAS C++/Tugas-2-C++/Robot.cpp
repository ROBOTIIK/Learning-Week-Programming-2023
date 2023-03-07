#include<iostream>
#include"Robot.h"
using namespace std;

int xBaru = 0, yBaru = 0;

void Robot::setKoordinat(int& x, int& y){
        if (x == 0 && y == 0){
            // cout << "PUSAT\n";
            xBaru += x;
            yBaru += y;
        }else if (x == 0 && y > 0){
            // cout << "UTARA\n";
            xBaru += x;
            yBaru += y;
        }else if (x > 0 && y == 0){
            // cout << "TIMUR\n";
            xBaru += x;
            yBaru += y;
        }else if (x == 0 && y < 0){
            // cout << "SELATAN\n";
            xBaru += x;
            yBaru += y;
        }else if (x < 0 && y == 0){
            // cout << "BARAT\n";
            xBaru += x;
            yBaru += y;
        }else if (x == 0 && y == 0){
            // cout << "PUSAT\n";
            xBaru += x;
            yBaru += y;
        }else if (x > 0 && y > 0){
            // cout << "TIMUR LAUT\n";
            xBaru += x;
            yBaru += y;
        }else if (x > 0 && y < 0){
            // cout << "TENGGARA\n";
            xBaru += x;
            yBaru += y;
        }else if (x < 0 && y < 0){
            // cout << "BARAT DAYA\n";
            xBaru += x;
            yBaru += y;
        }else if (x < 0 && y > 0){
            // cout << "BARAT LAUT\n";
            xBaru += x;
            yBaru += y;
        }    
}

void Robot::cetak(){
    cout << "Hasil Akhir Koordinat : (" << xBaru << "," << yBaru <<")\n";
}