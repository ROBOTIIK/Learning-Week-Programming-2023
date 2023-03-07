#include <iostream>
#include <vector>
#include "Robot.h"

int main() {
    int n;
    std::cin >> n;

    Robot robot;

    for (int i = 0; i < n; i++) {
        int x, y;
        std::cin >> x >> y;
        robot.move(x, y);
        std::cout << robot.getDirection() << std::endl;
    }

    auto position = robot.getPosition();
    std::cout << "KOORDINAT AKHIR: (" << position.first << ", " << position.second << ")" << std::endl;

    return 0;
}
