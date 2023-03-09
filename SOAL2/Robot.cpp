#include "Robot.h"

Robot::Robot() : x(0), y(0), direction("UTARA") {}

void Robot::move(int x, int y) {
    this->x += x;
    this->y += y;

    if (x > 0) {
        if (y > 0) {
            direction = "TIMUR LAUT";
        } else if (y < 0) {
            direction = "TIMUR SELATAN";
        } else {
            direction = "TIMUR";
        }
    } else if (x < 0) {
        if (y > 0) {
            direction = "BARAT LAUT";
        } else if (y < 0) {
            direction = "BARAT SELATAN";
        } else {
            direction = "BARAT";
        }
    } else {
        if (y > 0) {
            direction = "UTARA";
        } else if (y < 0) {
            direction = "SELATAN";
        }
    }
}

std::string Robot::getDirection() const {
    return direction;
}

std::pair<int, int> Robot::getPosition() const {
    return std::make_pair(x, y);
}