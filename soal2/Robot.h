#ifndef ROBOT_H
#define ROBOT_H

#include <string>

class Robot {
public:
    Robot(); // Constructor
    void move(int x, int y); // Method untuk memindahkan robot
    std::string getDirection() const; // Method untuk mendapatkan arah mata angin saat ini
    std::pair<int, int> getPosition() const; // Method untuk mendapatkan posisi robot saat ini
private:
    int x, y; // Koordinat robot
    std::string direction; // Arah mata angin saat ini
    void updateDirection(int x, int y); // Method untuk mengupdate arah mata angin saat robot bergerak
};

#endif
