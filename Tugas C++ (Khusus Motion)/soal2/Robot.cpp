#include <iostream>
#include "Robot.h"

Robot::Robot(int koordinatX, int koordinatY){
    koordinatX_ = koordinatX;
    koordinatY_ = koordinatY;
}

int Robot::getKoordinatX(){
    return koordinatX_;
}

int Robot::getKoordinatY(){
    return koordinatY_;
}

void Robot::setKoordinat(int x = 0, int y = 0){
    koordinatX_ += x;
    koordinatY_ += y;
}

void Robot::jalan(int x, int y){
    int xNow = getKoordinatX();
    int yNow = getKoordinatY();

    if(x > 0 && y > 0){
        std::cout << "TIMUR LAUT";
        setKoordinat(x,y);
    }
    else if(x > 0 && y < 0){
        std::cout << "TENGGARA";
        setKoordinat(x,y);
    }
    else if(x < 0 && y > 0){
        std::cout << "BARAT LAUT";
        setKoordinat(x,y);
    }
    else if(x < 0 && y < 0){
        std::cout << "BARAT DAYA";
        setKoordinat(x,y);
    }
    else if(x > 0 && y == 0){
        std::cout << "TIMUR";
        setKoordinat(x,y);
    }
    else if(x < 0 && y == 0){
        std::cout << "BARAT";
        setKoordinat(x,y);
    }
    else if(x == 0 && y > 0){
        std::cout << "UTARA";
        setKoordinat(x,y);
    }
    else if(x == 0 && y < 0){
        std::cout << "SELATAN";
        setKoordinat(x,y);
    }
    else{
        setKoordinat(x,y);
        std::cout << "Robot diam ditempat.";
    }
}