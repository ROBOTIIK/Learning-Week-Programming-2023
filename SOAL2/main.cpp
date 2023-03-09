#include <iostream>
#include <vector>
#include <utility>
#include "Robot.h"
#include "Robot.cpp"

int main() {
    int n;
    std::cin >> n;

    std::vector<std::pair<int, int>> moves(n);
    for (int i = 0; i < n; i++) {
        std::cin >> moves[i].first >> moves[i].second;
    }

    Robot robot;
    for (const auto& move : moves) {
        robot.move(move.first, move.second);
        std::cout << robot.getDirection() << std::endl;
    }

    auto position = robot.getPosition();
    std::cout << "KOORDINAT AKHIR: (" << position.first << ", " << position.second << ")" << std::endl;

    return 0;
}