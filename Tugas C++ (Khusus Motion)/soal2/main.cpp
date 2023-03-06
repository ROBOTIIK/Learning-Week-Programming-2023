#include <iostream>
#include "Robot.h"

int main(){
    int n, x, y;
    Robot Wall_E;
    std::cin >> n;

    for(int i = 0; i < n; i++){
        std::cin >> x >> y;
        Wall_E.jalan(x, y);
    }

    std::cout << "KOORDINAT AKHIR: (" << Wall_E.getKoordinatX() << ", " << Wall_E.getKoordinatY() << ")";
}