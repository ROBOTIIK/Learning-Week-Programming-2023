#include "Robot.h"

Robot::Robot() {
    x = 0;
    y = 0;
    direction = "UTARA"; // Robot menghadap ke arah utara saat pertama kali dibuat
}

void Robot::move(int x, int y) {
    this->x += x;
    this->y += y;
    updateDirection(x, y);
}

std::string Robot::getDirection() const {
    return direction;
}

std::pair<int, int> Robot::getPosition() const {
    return std::make_pair(x, y);
}

void Robot::updateDirection(int x, int y) {
    if (x > 0 && y == 0) {
        direction = "TIMUR";
    } else if (x < 0 && y == 0) {
        direction = "BARAT";
    } else if (x == 0 && y > 0) {
        direction = "UTARA";
    } else if (x == 0 && y < 0) {
        direction = "SELATAN";
    } else if (x > 0 && y > 0) {
        direction = "TIMUR LAUT";
    } else if (x < 0 && y > 0) {
        direction = "BARAT LAUT";
    } else if (x < 0 && y < 0) {
        direction = "BARAT DAYA";
    } else {
        direction = "TIMUR DAYA";
    }
}
