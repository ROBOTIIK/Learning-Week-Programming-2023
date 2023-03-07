#ifndef ROBOT
#define ROBOT

class Robot{
private:
    int x, y;
public:
    Robot(){};
    void setKoordinat(int& x, int& y);
    void cetak();
};

#endif