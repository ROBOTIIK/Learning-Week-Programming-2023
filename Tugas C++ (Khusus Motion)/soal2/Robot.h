#ifndef ROBOT
#define ROBOT

class Robot
{
public:
    Robot(int koordinatX = 0, int koordinatY = 0);
    int getKoordinatX();
    int getKoordinatY();
    void setKoordinat(int x, int y);

    void jalan(int x, int y);

private:
    int koordinatX_;
    int koordinatY_;
};

#endif