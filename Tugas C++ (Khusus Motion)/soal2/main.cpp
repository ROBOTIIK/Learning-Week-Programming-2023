#include <iostream>
#include "Robot.h"

int main() {
    Robot myRobot;
    int n, x, y;

    std::cin >> n; // Query user for how many input
    std::cout << std::endl;

    for (int i = 0; i < n; i++) {
        std::cin >> x >> y; // Query myRobot's movement
        myRobot.printDirection(x, y);
        myRobot.updateCoords(x, y);
    }

    int* coords = myRobot.getCoords();
    x = coords[0], y = coords[1]; // Assign current myRobot's coordinates to x and y
    std::cout << "KOORDINAT AKHIR: (" << x << ", " << y << ")" << std::endl;
}