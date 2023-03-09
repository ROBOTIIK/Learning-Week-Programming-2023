#ifndef ROBOT_H
#define ROBOT_H
#include <string>

class Robot {
public:
    Robot(); 
    void move(int x, int y); 
    std::string getDirection() const; 
    std::pair<int, int> getPosition() const; 
private:
    int x, y; 
    std::string direction; 
};

#endif