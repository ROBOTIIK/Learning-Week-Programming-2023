#include <iostream>
#include "Robot.h"

// Return array containing Robot's latest coords
int* Robot::getCoords() {
    int* coords = new int[2];                   // Declare an array to contain Robot's latest coords
    coords[0] = x_coord, coords[1] = y_coord;
    return coords;
}

// Print movement direction given x and y shifts
void Robot::printDirection(int x, int y) {

    if (x == 0) {
        if (y > 0)      std::cout << "UTARA";
        else if (y < 0) std::cout << "SELATAN";
        // else            std::cout << "DIAM";
    } else if (x > 0) {
        if (y > 0)      std::cout << "TIMUR LAUT";
        else if (y < 0) std::cout << "TENGGARA";
        else            std::cout << "TIMUR";
    }
    else {
        if (y > 0)      std::cout << "BARAT LAUT";
        else if (y < 0) std::cout << "BARAT DAYA";
        else            std::cout << "BARAT";
    }
    std::cout << "\n" << std::endl;
}

// Update Robot's coords given x and y shifts
void Robot::updateCoords(int x, int y) {
    x_coord += x;
    y_coord += y;
}