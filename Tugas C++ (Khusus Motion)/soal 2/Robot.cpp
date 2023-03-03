#include "Robot.h"
#include <iostream>
#include <string>

using namespace std;

optimus::optimus()
{
    console();
    printer();
}

void optimus::console()
{
    cin >> loop;
    for (int i = 0; i < loop; i++)
    {
        cin >> x >> y;
        track(i, x, y);
        compute(x, y);
    }
    cout << endl;
    
}

void optimus::track(int index, int a, int b){
    if (a > 0 && b == 0)
    {
        arah[index] = "TIMUR";
    }else if (a < 0 && b == 0)
    {
        arah[index] = "BARAT";
    }else if (a == 0 && b > 0)
    {
        arah[index] = "UTARA";
    }else if (a == 0 && b < 0)
    {
        arah[index] = "SELATAN";
    }else if (a < 0 && b < 0)
    {
        arah[index] = "BARAT DAYA";
    }else if (a < 0 && b > 0)
    {
        arah[index] = "BARAT LAUT";
    }else if (a > 0 && b > 0)
    {
        arah[index] = "TIMUR LAUT";
    }else if (a > 0 && b < 0)
    {
        arah[index] = "TENGGARA";
    }
}

void optimus::compute(int c, int d){
    xe += c;
    ye += d;
}

void optimus::printer(){
    for (int j = 0; j < loop; j++)
    {
        cout << arah[j] << endl;
    }
    cout << "KOORDINAT AKHIR: (" << xe << ", " << ye << ")" << endl;
    
}